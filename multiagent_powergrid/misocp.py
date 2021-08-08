import numpy as np
import pandapower as pp
from pyscipopt import Model, quicksum
from networks.ieee34 import IEEE34Bus
from matplotlib import pyplot as plt
from pandapower.pypower.idx_bus import BUS_I, BASE_KV, PD, QD, GS, BS, VMAX, VMIN, BUS_TYPE, NONE, VM, VA, \
    CID, CZD, bus_cols, REF
from pandapower.pypower.idx_brch import F_BUS, T_BUS, BR_R, BR_X, BR_B, TAP, SHIFT, BR_STATUS, RATE_A, \
    BR_R_ASYM, BR_X_ASYM, branch_cols

def read_data():
    import pickle, os
    f = open(os.path.join('../data','data2018-2020.pkl'), 'rb')
    data = pickle.load(f)
    f.close()
    return data

dataset = read_data()
price = dataset['test']['price'].reshape([366,24])
load_scale = dataset['test']['load'].reshape([366,24])
solar_scale = dataset['test']['solar'].reshape([366,24])
wind_scale = dataset['test']['wind'].reshape([366,24])

net = IEEE34Bus()
net.p_mw = 0
net.q_mvar = 0

pp.runpp(net)
net.sgen.scaling = 0
ppc = net._ppc
eps = np.finfo(np.float32).eps

n_buses = ppc['bus'].shape[0]
n_lines = ppc['branch'].shape[0]

id2bus = dict(zip(net.bus.index.tolist(), net.bus['name'].values))
bus2id = dict(zip(net.bus['name'].values, net.bus.index.tolist()))

bus2vr = {}
for idx, trafo in net.trafo.iterrows():
    if 'Regulator' in trafo['name']:
        hv, lv = trafo[['hv_bus','lv_bus']].values
        bus2vr[hv, lv] = idx

bus2cap = {}
bus2cap = dict(zip(net.shunt['bus'].values, net.shunt['bus'].index))

r = ppc['branch'][:,BR_R].real
x = ppc['branch'][:,BR_X].real
z = np.sqrt(r**2 + x**2)
l_ub = np.array(net.line.max_i_ka.tolist()+[0.18, 0.18, 0.5]) * 24.9
f_bus = ppc['branch'][:,F_BUS].real[:n_lines]
t_bus = ppc['branch'][:,T_BUS].real[:n_lines]

pd = ppc['bus'][:,PD]
qd = ppc['bus'][:,QD]

vmax = 1.05
vmin = 0.95

time_steps = 24
cost, schedues = [], {}
es_0 = 0.5
for d in range(366):
    model = Model("IEEE34")
    # Define gen variables
    PG, QG = {}, {}
    DG1_cost, DG2_cost, GRID_cost = {}, {}, {}
    for t in range(time_steps):
        PG[t, bus2id['Bus 800']] = P_GRID_T = model.addVar(lb=-2.5, ub=2.5, vtype="C", name="PG_Bus_800_{}".format(t))
        QG[t, bus2id['Bus 800']] = Q_GRID_T = model.addVar(lb=-2.5, ub=2.5, vtype="C", name="QG_Bus 800_{}".format(t))
        PG[t, bus2id['Bus 848']] = P_DG1_T = model.addVar(lb=0, ub=0.66, vtype="C", name="PG_Bus 848_{}".format(t))
        QG[t, bus2id['Bus 848']] = Q_DG1_T = model.addVar(lb=-0.5, ub=0.5, vtype="C", name="QG_Bus 848_{}".format(t))
        PG[t, bus2id['Bus 890']] = P_DG2_T = model.addVar(lb=0, ub=0.5, vtype="C", name="PG_Bus 890_{}".format(t))
        QG[t, bus2id['Bus 890']] = Q_DG2_T = model.addVar(lb=-0.375, ub=0.375, vtype="C", name="QG_Bus 890_{}".format(t))
        PG[t, bus2id['Bus 822']] = 0.1 * solar_scale[d,t]
        PG[t, bus2id['Bus 856']] = 0.1 * solar_scale[d,t]
        PG[t, bus2id['Bus 838']] = 0.1 * solar_scale[d,t]
        PG[t, bus2id['Bus 822']] = 0.1 * wind_scale[d,t]
        PG[t, bus2id['Bus 826']] = 0.1 * wind_scale[d,t]
        PG[t, bus2id['Bus 838']] = 0.1 * wind_scale[d,t]
        model.addCons(P_GRID_T**2 + Q_GRID_T**2 <= 2.5**2, name="Sub_capacity_cons_{}".format(t))
        model.addCons(P_DG1_T/np.tan(np.arccos(-np.sqrt(1-0.8**2))) <= Q_DG1_T, name="DG1_min_pf_cons_{}".format(t))
        model.addCons(P_DG1_T/np.tan(np.arccos(np.sqrt(1-0.8**2))) >= Q_DG1_T, name="DG1_max_pf_cons_{}".format(t))
        model.addCons(P_DG2_T/np.tan(np.arccos(-np.sqrt(1-0.8**2))) <= Q_DG2_T, name="DG1_min_pf_cons_{}".format(t))
        model.addCons(P_DG2_T/np.tan(np.arccos(np.sqrt(1-0.8**2))) >= Q_DG2_T, name="DG1_max_pf_cons_{}".format(t))
        # Define cost
        a1, b1, c1 = 100, 72.4, 0.5011
        a2, b2, c2 = 100, 51.6, 0.4615
        DG1_cost[t] = model.addVar(vtype="C", name="DG1_cost_{}".format(t))
        DG2_cost[t] = model.addVar(vtype="C", name="DG2_cost_{}".format(t))
        GRID_cost[t] = model.addVar(vtype="C", name="GRID_cost_{}".format(t))
        model.addCons(DG1_cost[t] == a1*(P_DG1_T**2) + b1*P_DG1_T + c1, name="DG1_cost_cons_{}".format(t)) # ($)
        model.addCons(DG2_cost[t] == a2*(P_DG2_T**2) + b2*P_DG2_T + c2, name="DG2_cost_cons_{}".format(t)) # ($)
        model.addCons(GRID_cost[t] == price[d,t] * P_GRID_T, name="GRID_cost_cons_{}".format(t))
    # # Define storage variables
    eta_ch, eta_dch = 0.98, 0.98
    max_es, min_es, max_p = 2.0, 0.2, 0.5
    PS_CH, PS_DCH, BS, ES = {}, {}, {}, {}
    for t in range(time_steps):
        PS_CH[t,bus2id['Bus 810']] = PS1_CH_T = model.addVar(vtype="C", name="PS_CH_{}".format(t))
        PS_DCH[t,bus2id['Bus 810']] = PS1_DCH_T = model.addVar(vtype="C", name="PS_DCH_{}".format(t))
        BS[t,bus2id['Bus 810']] = BS1_T = model.addVar(vtype="B", name="BS_{}".format(t))
        ES[t,bus2id['Bus 810']] = ES1_T = model.addVar(lb=0.2, ub=2, vtype="C", name="ES_{}".format(t))
        model.addCons(PS1_CH_T <= max_p * BS1_T)
        model.addCons(PS1_CH_T >= 0.0 * BS1_T)
        model.addCons(PS1_DCH_T <= max_p * (1 - BS1_T))
        model.addCons(PS1_DCH_T >= 0.0 * (1 - BS1_T))
        if t == 0:
            model.addCons(ES1_T == es_0 + PS1_CH_T*eta_ch - PS1_DCH_T/eta_ch)
        else:
            model.addCons(ES1_T == ES[t-1,bus2id['Bus 810']] + PS1_CH_T*eta_ch - PS1_DCH_T/eta_ch)
    # Define variables I^{2}
    I_SR, P_IJ, Q_IJ = {}, {}, {}
    for t in range(time_steps):
        for k in range(n_lines):
            I_SR[t,k] = model.addVar(lb=0, ub=l_ub[k]**2, vtype="C", name="I_SR_{}_{}".format(k,t))
            P_IJ[t,k] = model.addVar(lb=-10, ub=10, vtype="C", name="P_IJ_{}_{}".format(k,t))
            Q_IJ[t,k] = model.addVar(lb=-10, ub=10, vtype="C", name="Q_IJ_{}_{}".format(k,t))
    # Define variables V^{2}
    V_SR = {}
    for t in range(time_steps):
        for i in range(n_buses):
            if ppc['bus'][i,BUS_TYPE] == 3: # reference bus
                V_SR[t,i] = 1.0 # model.addVar(lb=1-eps, ub=1+eps, vtype="C", name="V_SR_{}".format(i))
            else:
                V_SR[t,i] = model.addVar(lb=vmin**2, ub=vmax**2, vtype="C", name="V_SR_{}_{}".format(i,t))
    # Define VR variables
    VR_TAP = {}
    for t in range(time_steps):
        for (fbus,tbus), v in bus2vr.items():
            lb, ub = net.trafo.loc[v].tap_min, net.trafo.loc[v].tap_max
            VR_TAP[t,v] = model.addVar(lb=lb, ub=ub, vtype="I", name=net.trafo.loc[v]['name']+"_{}".format(t))
    # Define shunt capacitor variables
    CAP = {}
    for t in range(time_steps):
        for b, c in bus2cap.items():
            lb, ub = 0, net.shunt.loc[c].max_step
            CAP[t,c] = model.addVar(lb=lb, ub=ub, vtype="I", name=net.shunt.loc[c]['name']+"_{}".format(t))
    # Define dist flow constraints
    for t in range(time_steps):
        for i in range(n_buses):
            # load flow from upstream nodes
            SUM_P_KI, SUM_Q_KI = 0.0, 0.0
            for k in np.where(t_bus==i)[0]:
                SUM_P_KI += P_IJ[t,k] - r[k]*I_SR[t,k]
                SUM_Q_KI += Q_IJ[t,k] - x[k]*I_SR[t,k]
            # load flow from downstream nodes
            SUM_P_IJ, SUM_Q_IJ = 0.0, 0.0
            for j in np.where(f_bus==i)[0]:
                SUM_P_IJ += P_IJ[t,j]
                SUM_Q_IJ += Q_IJ[t,j]
            # power injection into node i
            PG_I = PG.get((t,i)) or 0.0
            QG_I = QG.get((t,i)) or 0.0
            PS_I = PS_DCH.get((t,i)) or 0.0
            PS_I -= PS_CH.get((t,i)) or 0.0
            CAP_I = CAP[t,bus2cap[i]]*net.shunt.loc[bus2cap[i]].q_mvar if bus2cap.get(i) is not None else 0.0
            model.addCons(PG_I + PS_I - pd[i]*load_scale[d,t] == SUM_P_IJ - SUM_P_KI)
            model.addCons(QG_I - CAP_I - qd[i]*load_scale[d,t] == SUM_Q_IJ - SUM_Q_KI)
    # Define dist flow constraints
    for t in range(time_steps):
        for ij in range(n_lines):
            i = int(f_bus[ij])
            j = int(t_bus[ij])
            if bus2vr.get((i,j)):
                v = bus2vr.get((i,j))
                tap_step_percent = net.trafo.loc[v].tap_step_percent
                tap_neutral = net.trafo.loc[v].tap_neutral
                tap_step = (VR_TAP[t,v] - tap_neutral) * tap_step_percent / 100
                ratio = 1 + tap_step if net.trafo.loc[v].tap_side == 'lv' else 1 / (1 + tap_step)
            else:
                ratio = 1
            model.addCons(V_SR[t,j]*(ratio*ratio) == V_SR[t,i] - 2*(r[ij]*P_IJ[t,ij] + x[ij]*Q_IJ[t,ij]) + z[ij]*z[ij]*I_SR[t,ij])
            model.addCons(I_SR[t,ij]*V_SR[t,i] >= P_IJ[t,ij]*P_IJ[t,ij] + Q_IJ[t,ij]*Q_IJ[t,ij])
    model.setObjective(quicksum(DG1_cost[t]+DG2_cost[t]+GRID_cost[t] for t in range(time_steps)))
    model.hideOutput()
    model.setRealParam('limits/time', 300)
    model.optimize()
    obj = model.getObjVal()
    sol = model.getBestSol()
    print('Day {} is done!'.format(d))
    cost.append(obj)

    v_pu = np.empty([time_steps, n_buses])
    for t in range(time_steps):
        for i in range(1, n_buses):
            v_pu[t,i] = np.sqrt(sol[V_SR[t,i]])
    i_pu = np.empty([time_steps, n_lines])
    for t in range(time_steps):
        for ij in range(1, n_lines):
            i_pu[t,ij] = np.sqrt(sol[I_SR[t,ij]])
    cap1 = np.empty([time_steps])
    for t in range(time_steps):
        cap1[t] = sol[CAP[t,0]]
    cap2 = np.empty([time_steps])
    for t in range(time_steps):
        cap2[t] = sol[CAP[t,1]]
    vr_tap1 = np.empty([time_steps])
    for t in range(time_steps):
        vr_tap1[t] = sol[VR_TAP[t,0]]
    vr_tap2 = np.empty([time_steps])
    for t in range(time_steps):
        vr_tap2[t] = sol[VR_TAP[t,1]]
    p_dg1, q_dg1 = np.empty([time_steps]), np.empty([time_steps])
    for t in range(time_steps):
        p_dg1[t] = sol[PG[t,bus2id['Bus 848']]]
        q_dg1[t] = sol[QG[t,bus2id['Bus 848']]]
    p_dg2, q_dg2 = np.empty([time_steps]), np.empty([time_steps])
    for t in range(time_steps):
        p_dg2[t] = sol[PG[t,bus2id['Bus 890']]]
        q_dg2[t] = sol[QG[t,bus2id['Bus 890']]]
    p_grid, q_grid = np.empty([time_steps]), np.empty([time_steps])
    for t in range(time_steps):
        p_grid[t] = sol[PG[t,bus2id['Bus 800']]]
        q_grid[t] = sol[QG[t,bus2id['Bus 800']]]
    p_s, e_s = np.empty([time_steps]), np.empty([time_steps])
    for t in range(time_steps):
        p_s[t] = sol[PS_DCH[t,bus2id['Bus 810']]] - sol[PS_CH[t,bus2id['Bus 810']]]
        e_s[t] = sol[ES[t,bus2id['Bus 810']]]
    es_0 = e_s[-1]
    p_renew = []
    for t in range(time_steps):
        p = PG[t,bus2id['Bus 822']] * solar_scale[d,t] + \
            PG[t,bus2id['Bus 856']] * solar_scale[d,t] + \
            PG[t,bus2id['Bus 838']] * solar_scale[d,t] + \
            PG[t,bus2id['Bus 822']] * wind_scale[d,t] + \
            PG[t,bus2id['Bus 826']] * wind_scale[d,t] + \
            PG[t,bus2id['Bus 838']] * wind_scale[d,t]
        p_renew.append(p)
    # for t in range(time_steps):
    #     print(p_grid[t]+p_dg1[t]+p_dg2[t]+p_renew[t]+p_s[t], np.sum(pd * load_scale[d,t]))
    #     print(q_grid[t]+q_dg1[t]+q_dg2[t]-cap1[t]*0.12-cap2[t]*0.12, np.sum(qd * load_scale[d,t]))
    # dg1_cost, dg2_cost, grid_cost = 0, 0, 0
    # for t in range(time_steps):
    #     dg1_cost += a1 * (p_dg1[t]**2) + b1 * p_dg1[t] + c1
    #     dg2_cost += a2 * (p_dg2[t]**2) + b2 * p_dg2[t] + c2
    #     grid_cost += price[d,t] * p_grid[t]
    # print(dg1_cost+dg2_cost+grid_cost)

    schedues[d] = {
        'grid_P': p_grid, 
        'grid_Q': q_grid, 
        'DG1_P': p_dg1, 
        'DG1_Q': q_dg1, 
        'DG2_P': p_dg2, 
        'DG2_Q': q_dg2, 
        'ESS_E': e_s, 
        'ESS_P': p_s, 
        'VR1': vr_tap1,
        'VR2': vr_tap2,
        'SCB1': cap1,
        'SCB2': cap2,
        'voltage': v_pu, 
        'current': i_pu, 
    }


import pickle, os
save_path = '/home/lihepeng/Documents/Github/learning2opDN/results/test/misocp.pkl'
with open(save_path, 'wb') as f:
    pickle.dump({'cost': cost, 'schedues': schedues}, f, protocol=pickle.HIGHEST_PROTOCOL)
print('done')



import pickle, os
save_path = '/home/lihepeng/Documents/Github/learning2opDN/results/test/misocp.pkl'
with open(save_path, 'rb') as f:
    data = pickle.load(f)

print('done')

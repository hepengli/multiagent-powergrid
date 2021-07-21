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

time_steps = 24
d = 0
dataset = read_data()
price = dataset['test']['price'].reshape([366,time_steps])
load_scale = dataset['test']['load'].reshape([366,time_steps])
solar_scale = dataset['test']['solar'].reshape([366,time_steps])
wind_scale = dataset['test']['wind'].reshape([366,time_steps])

net = IEEE34Bus()

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
l_ub = np.array(net.line.max_i_ka.tolist()+[0.18, 0.18, 0.18])*1.5
f_bus = ppc['branch'][:,F_BUS].real
t_bus = ppc['branch'][:,T_BUS].real

pd = ppc['bus'][:,PD]
qd = ppc['bus'][:,QD]

vmax = 1.05
vmin = 0.95

time_steps = 24
cost = []
for d in range(1,2):
    model = Model("IEEE34")
    # Define gen variables
    PG, QG = {}, {}
    DG1_cost, DG2_cost, GRID_cost = {}, {}, {}
    for t in range(time_steps):
        PG[t, bus2id['Bus 800']] = model.addVar(vtype="C", name="PG_Bus_800_{}".format(t))
        QG[t, bus2id['Bus 800']] = model.addVar(vtype="C", name="QG_Bus 800_{}".format(t))
        PG[t, bus2id['Bus 848']] = model.addVar(lb=0, ub=0.66, vtype="C", name="PG_Bus 848_{}".format(t))
        QG[t, bus2id['Bus 848']] = model.addVar(lb=-0.5, ub=0.5, vtype="C", name="QG_Bus 848_{}".format(t))
        PG[t, bus2id['Bus 890']] = model.addVar(lb=0, ub=0.5, vtype="C", name="PG_Bus 890_{}".format(t))
        QG[t, bus2id['Bus 890']] = model.addVar(lb=-0.375, ub=0.375, vtype="C", name="QG_Bus 890_{}".format(t))
        PG[t, bus2id['Bus 822']] = 0.1 * solar_scale[d,t]
        PG[t, bus2id['Bus 856']] = 0.1 * solar_scale[d,t]
        PG[t, bus2id['Bus 838']] = 0.1 * solar_scale[d,t]
        PG[t, bus2id['Bus 822']] = 0.1 * wind_scale[d,t]
        PG[t, bus2id['Bus 826']] = 0.1 * wind_scale[d,t]
        PG[t, bus2id['Bus 838']] = 0.1 * wind_scale[d,t]

        model.addCons(PG[t, bus2id['Bus 800']]**2 + QG[t, bus2id['Bus 800']]**2 <= 2.5**2, name="Sub_capacity_cons_{}".format(t))

        DG1_min_pf = 0.8
        model.addCons(PG[t, bus2id['Bus 848']] / np.tan(np.arccos(-np.sqrt(1-DG1_min_pf**2))) <= \
            QG[t, bus2id['Bus 848']], name="DG1_min_pf_cons_{}".format(t))
        model.addCons(PG[t, bus2id['Bus 848']] / np.tan(np.arccos(np.sqrt(1-DG1_min_pf**2))) >= \
            QG[t, bus2id['Bus 848']], name="DG1_max_pf_cons_{}".format(t))

        DG2_min_pf = 0.8
        model.addCons(PG[t, bus2id['Bus 890']] / np.tan(np.arccos(-np.sqrt(1-DG2_min_pf**2))) <= \
            QG[t, bus2id['Bus 890']], name="DG2_min_pf_cons_{}".format(t))
        model.addCons(PG[t, bus2id['Bus 890']] / np.tan(np.arccos(np.sqrt(1-DG2_min_pf**2))) >= \
            QG[t, bus2id['Bus 890']], name="DG2_max_pf_cons_{}".format(t))

        # Define cost
        a1, b1, c1 = 100, 72.4, 0.5011
        a2, b2, c2 = 100, 51.6, 0.4615
        DG1_cost[t] = model.addVar(vtype="C", name="DG1_cost_{}".format(t))
        DG2_cost[t] = model.addVar(vtype="C", name="DG2_cost_{}".format(t))
        GRID_cost[t] = model.addVar(vtype="C", name="GRID_cost_{}".format(t))

        model.addCons(DG1_cost[t] == a1*(PG[t, bus2id['Bus 848']]**2) + b1*PG[t, bus2id['Bus 848']] + c1, name="DG1_cost_cons_{}".format(t)) # ($)
        model.addCons(DG2_cost[t] == a2*(PG[t, bus2id['Bus 890']]**2) + b2*PG[t, bus2id['Bus 890']] + c2, name="DG2_cost_cons_{}".format(t)) # ($)
        model.addCons(GRID_cost[t] == price[d,t] * PG[t, bus2id['Bus 800']], name="GRID_cost_cons_{}".format(t))

    # # Define storage variables
    ES_0, max_p, eta_ch, eta_dch, delta_t = 0.5, 0.5, 0.98, 0.98, 1
    PS_CH, PS_DCH, BS, ES = {}, {}, {}, {}
    for t in range(time_steps):
        PS_CH[t,bus2id['Bus 810']] = model.addVar(vtype="C", name="PS_CH_{}".format(t))
        PS_DCH[t,bus2id['Bus 810']] = model.addVar(vtype="C", name="PS_DCH_{}".format(t))
        BS[t,bus2id['Bus 810']] = model.addVar(vtype="B", name="BS_{}".format(t))
        ES[t,bus2id['Bus 810']] = model.addVar(lb=0.2, ub=2, vtype="C", name="ES_{}".format(t))

        model.addCons(PS_CH[t,bus2id['Bus 810']] <= max_p * BS[t,bus2id['Bus 810']])
        model.addCons(PS_CH[t,bus2id['Bus 810']] >= 0.0 * BS[t,bus2id['Bus 810']])
        model.addCons(PS_DCH[t,bus2id['Bus 810']] <= max_p * (1 - BS[t,bus2id['Bus 810']]))
        model.addCons(PS_DCH[t,bus2id['Bus 810']] >= 0.0 * (1 - BS[t,bus2id['Bus 810']]))
        if t == 0:
            model.addCons(ES[t,bus2id['Bus 810']] == ES_0 + \
                (PS_CH[t,bus2id['Bus 810']]*eta_ch - PS_DCH[t,bus2id['Bus 810']]/eta_ch)*delta_t)
        else:
            model.addCons(ES[t,bus2id['Bus 810']] == ES[t-1,bus2id['Bus 810']] + \
                (PS_CH[t,bus2id['Bus 810']]*eta_ch - PS_DCH[t,bus2id['Bus 810']]/eta_ch)*delta_t)

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
            CAP_I = CAP[t,bus2cap[i]] * net.shunt.loc[bus2cap[i]].q_mvar if bus2cap.get(i) is not None else 0.0
            model.addCons(PG_I + PS_I - pd[i]*load_scale[d,t] == SUM_P_IJ - SUM_P_KI)
            model.addCons(QG_I - CAP_I - qd[i]*load_scale[d,t] == SUM_Q_IJ - SUM_Q_KI)

    # Define VR variables
    VR_TAP = {}
    for t in range(time_steps):
        for (fbus,tbus), v in bus2vr.items():
            lb, ub = net.trafo.loc[v].tap_min, net.trafo.loc[v].tap_max
            VR_TAP[t,v] = model.addVar(lb=lb, ub=ub, vtype="I", name=net.trafo.loc[v]['name']+"_{}".format(t))

    # Define dist flow constraints
    for t in range(time_steps):
        for ij in range(n_lines):
            i = int(f_bus[ij])
            j = int(t_bus[ij])
            if bus2vr.get((i,j)):
                tap_step_percent = net.trafo.loc[bus2vr[i,j]].tap_step_percent
                tap_neutral = net.trafo.loc[bus2vr[i,j]].tap_neutral
                tap_step = (VR_TAP[t,bus2vr[i,j]] - tap_neutral) * tap_step_percent / 100
                ratio = 1 / (1 + tap_step) if net.trafo.loc[0].tap_side == 'lv' else (1 + tap_step)
            else:
                ratio = 1
            model.addCons(V_SR[t,j]/(ratio**2) == V_SR[t,i] - 2*(r[ij]*P_IJ[t,ij] + x[ij]*Q_IJ[t,ij]) + z[ij]*z[ij]*I_SR[t,ij])
            model.addCons(I_SR[t,ij] * V_SR[t,i] == P_IJ[t,ij]*P_IJ[t,ij] + Q_IJ[t,ij]*Q_IJ[t,ij])

    model.setObjective(quicksum(DG1_cost) + quicksum(DG2_cost) + quicksum(GRID_cost))

    # model.hideOutput()
    # model.setRealParam('limits/time', 60)
    model.optimize()
    sol = model.getBestSol()
    print('Day {} is finished.'.format(d))

    # # print('\nBus voltage:')
    # for t in range(time_steps):
    #     for i in range(1, n_buses):
    #         print(np.sqrt(sol[V_SR[t,i]]))

    # # print('\nBranch power flow:')
    # for t in range(time_steps):
    #     for ij in range(1, n_lines):
    #         print(np.sqrt(sol[I_SR[t,ij]]))

    # for t in range(time_steps):
    #     for i in range(1, n_lines):
    #         print(sol[P_IJ[t,i]])

    q_cap1 = []
    for t in range(time_steps):
        q_cap1.append(sol[CAP[t,0]]*net.shunt.loc[0].q_mvar)

    q_cap2 = []
    for t in range(time_steps):
        q_cap2.append(sol[CAP[t,1]]*net.shunt.loc[1].q_mvar)

    # for t in range(time_steps):
    #     for (fbus,tbus), v in bus2vr.items():
    #         print(sol[VR_TAP[t,v]])

    # print('\nOptimal charging:')
    p_s = []
    for t in range(time_steps):
        p_s.append(sol[PS_DCH[t,bus2id['Bus 810']]] - sol[PS_CH[t,bus2id['Bus 810']]])

    p_dg1, q_dg1 = [], []
    for t in range(time_steps):
        p_dg1.append(sol[PG[t,bus2id['Bus 848']]])
        q_dg1.append(sol[QG[t,bus2id['Bus 890']]])

    p_dg2, q_dg2 = [], []
    for t in range(time_steps):
        p_dg2.append(sol[PG[t,bus2id['Bus 890']]])
        q_dg2.append(sol[QG[t,bus2id['Bus 890']]])

    p_grid, q_grid = [], []
    for t in range(time_steps):
        p_grid.append(sol[PG[t,bus2id['Bus 800']]])
        q_grid.append(sol[QG[t,bus2id['Bus 800']]])

    p_renew = []
    for t in range(time_steps):
        p = PG[t,bus2id['Bus 822']] + \
            PG[t,bus2id['Bus 856']] + \
            PG[t,bus2id['Bus 838']] + \
            PG[t,bus2id['Bus 822']] + \
            PG[t,bus2id['Bus 826']] + \
            PG[t,bus2id['Bus 838']]
        p_renew.append(p)

    for t in range(time_steps):
        print(p_grid[t]+p_dg1[t]+p_dg2[t]+p_renew[t]+p_s[t], np.sum(pd * load_scale[d,t]))
        print(q_grid[t]+q_dg1[t]+q_dg2[t]-q_cap1[t]-q_cap2[t], np.sum(qd * load_scale[d,t]))

    dg1_cost, dg2_cost, grid_cost = 0, 0, 0
    for t in range(time_steps):
        dg1_cost += a1 * (p_dg1[t]**2) + b1 * p_dg1[t] + c1
        dg2_cost += a2 * (p_dg2[t]**2) + b2 * p_dg2[t] + c2
        grid_cost += price[d,t] * p_grid[t]

    cost.append(dg1_cost+dg2_cost+grid_cost)
    print(cost)


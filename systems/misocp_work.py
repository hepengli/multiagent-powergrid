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

eps = np.finfo(np.float32).eps

time_steps = 24
dataset = read_data()
price = dataset['test']['price'].reshape([366,time_steps])
load_scale = dataset['test']['load'].reshape([366,time_steps])
solar_scale = dataset['test']['solar'].reshape([366,time_steps])
wind_scale = dataset['test']['wind'].reshape([366,time_steps])

net = IEEE34Bus()

pp.runpp(net)
net.sgen.scaling = 0
ppc = net._ppc

n_buses = ppc['bus'].shape[0]
n_lines = ppc['branch'].shape[0]

id2bus = dict(zip(net.bus.index.tolist(), net.bus['name'].values))
bus2id = dict(zip(net.bus['name'].values, net.bus.index.tolist()))

r = ppc['branch'][:,BR_R].real
x = ppc['branch'][:,BR_X].real
z = np.sqrt(r**2 + x**2)
l_ub = ppc['branch'][:,RATE_A].real * 6e-4
f_bus = ppc['branch'][:,F_BUS].real
t_bus = ppc['branch'][:,T_BUS].real

pd = ppc['bus'][:,PD] * 0.1
qd = ppc['bus'][:,QD] * 0.1

vmax = 1.05
vmin = 0.95

time_steps = 1
cost = []
model = Model("IEEE34")
# Define gen variables
PG, QG = {}, {}
DG1_cost, DG2_cost, GRID_cost = {}, {}, {}
for t in range(time_steps):
    PG[t, bus2id['Bus 800']] = model.addVar(lb=-2.5,   ub=2.5,   vtype="C", name="PG_Bus_800_{}".format(t))
    QG[t, bus2id['Bus 800']] = model.addVar(lb=-2.5,   ub=2.5,   vtype="C", name="QG_Bus 800_{}".format(t))

    # Define cost
    GRID_cost[t] = model.addVar(vtype="C", name="GRID_cost_{}".format(t))

    model.addCons(GRID_cost[t] == price[0,t] * PG[t, bus2id['Bus 800']], name="GRID_cost_cons_{}".format(t))

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

# Define dist flow constraints
for t in range(time_steps):
    for i in range(n_buses):
        # load flow from upstream nodes
        SUM_P_KI, SUM_Q_KI = 0.0, 0.0
        for k in np.where(t_bus==i)[0]:
            SUM_P_KI += P_IJ[t,k] - r[k]*I_SR[t,k]
            SUM_Q_KI += Q_IJ[t,k] - x[k]*I_SR[t,k]
        # load flow to downstream nodes
        SUM_P_IJ, SUM_Q_IJ = 0.0, 0.0
        for j in np.where(f_bus==i)[0]:
            SUM_P_IJ += P_IJ[t,j]
            SUM_Q_IJ += Q_IJ[t,j]
        # power injection into node i
        PG_I = PG.get((t,i)) or 0.0
        QG_I = QG.get((t,i)) or 0.0
        model.addCons(PG_I - pd[i]*load_scale[0,t] == SUM_P_IJ - SUM_P_KI)
        model.addCons(QG_I - qd[i]*load_scale[0,t] == SUM_Q_IJ - SUM_Q_KI)

# Define dist flow constraints
for t in range(time_steps):
    for ij in range(n_lines):
        i = int(f_bus[ij])
        j = int(t_bus[ij])
        model.addCons(V_SR[t,j] == V_SR[t,i] - 2*(r[ij]*P_IJ[t,ij] + x[ij]*Q_IJ[t,ij]) + z[ij]*z[ij]*I_SR[t,ij])
        model.addCons(I_SR[t,ij] * V_SR[t,i] == P_IJ[t,ij]*P_IJ[t,ij] + Q_IJ[t,ij]*Q_IJ[t,ij])

model.setObjective(quicksum(GRID_cost))

# model.hideOutput()
# model.setRealParam('limits/time', 60)
model.optimize()
sol = model.getBestSol()
obj = model.getObjVal()

for t in range(time_steps):
    for i in range(1, n_buses):
        print(np.sqrt(sol[V_SR[t,i]]))
print()

for t in range(time_steps):
    for ij in range(1, n_lines):
        print(np.sqrt(sol[I_SR[t,ij]]))
print()

for t in range(time_steps):
    for i in range(1, n_lines):
        print(sol[P_IJ[t,i]])
print()

# print('\nOptimal capacity banks:')
# for t in range(time_steps):
#     for b, c in bus2cap.items():
#         print(sol[CAP[t,c]])

# print('\nOptimal tap positions:')
# for t in range(time_steps):
#     for (fbus,tbus), v in bus2vr.items():
#         print(sol[VR_TAP[t,v]])

# print('\nOptimal charging:')
# for t in range(time_steps):
#     print(sol[PS_CH[t,bus2id['Bus 810']]] - sol[PS_DCH[t,bus2id['Bus 810']]])

# # print('\nDG1 power:')
# pg_dg1 = []
# for t in range(time_steps):
#     pg_dg1.append(sol[PG[t,bus2id['Bus 848']]])
#     # print(sol[PG[t,bus2id['Bus 848']]])

# plt.plot(pg_dg1)
# plt.show()

# # print('\nDG2 power:')
# pg_dg2 = []
# for t in range(time_steps):
#     pg_dg2.append(sol[PG[t,bus2id['Bus 890']]])
#     # print(sol[PG[t,bus2id['Bus 890']]])

# plt.plot(pg_dg2)
# plt.show()

# print('\nGrid power:')
pg_grid = []
for t in range(time_steps):
    pg_grid.append(sol[PG[t,bus2id['Bus 800']]])
    # print(sol[PG[t,bus2id['Bus 800']]])

# plt.plot(pg_grid)
# plt.show()

print(obj)
print(pg_grid[0], np.sum(pd * load_scale[0,0]))


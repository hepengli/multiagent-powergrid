import numpy as np
import pandas as pd
import pandapower as pp
from collections import deque
from copy import deepcopy

import time
import gym
from gym import spaces
from gym.utils import seeding
from collections import deque
from .networks.ieee123 import IEEE123Bus
from .core import *

def read_data():
    import pickle, os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(os.path.dirname(dir_path), 'data','data2018-2020.pkl'), 'rb')
    data = pickle.load(f)
    f.close()
    return data

# environment for all agents in the multiagent world
# currently code assumes that no agents will be created/destroyed at runtime!
class IEEE123BusSystemDDPG(gym.Env):
    metadata = {
        'render.modes' : ['human', 'rgb_array']
    }

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.train = kwargs.get('train')
        self.AC = kwargs.get('AC') # AC power flow
        self.topology = kwargs.get('topology') # AC power flow
        self.dataset = read_data()['train'] if self.train else read_data()['test']
        self.total_timesteps = self.dataset['solar'].size
        self.total_days = self.dataset['solar'].size//24

        self.t = 0 # timestep counter
        self.dt = 1 # simulation timestep
        self.window = 24

        # network architecture
        self.net = IEEE123Bus()

        # seed
        self.seed()

        # list of agents
        DG_1 = DG('DG 1', bus='Bus 24',  min_p_mw=0, max_p_mw=0.66, sn_mva=0.825, control_q=True, cost_curve_coefs=[100, 51.6, 0.4615])
        # DG_2 = DG('DG 2', bus='Bus 41',  min_p_mw=0, max_p_mw=0.66, sn_mva=0.825, control_q=True, cost_curve_coefs=[100, 51.6, 0.4615])
        DG_3 = DG('DG 3', bus='Bus 94',  min_p_mw=0, max_p_mw=0.5,  sn_mva=0.625, control_q=True, cost_curve_coefs=[100, 72.4, 0.5011])
        DG_4 = DG('DG 4', bus='Bus 71',  min_p_mw=0, max_p_mw=0.5,  sn_mva=0.625, control_q=True, cost_curve_coefs=[100, 72.4, 0.5011])
        # DG_5 = DG('DG 5', bus='Bus 114', min_p_mw=0, max_p_mw=0.4,  sn_mva=0.5,   control_q=True, cost_curve_coefs=[100, 81.6, 0.3011])
        PV_1 = RES('PV 1', source='SOLAR', bus='Bus 22',  sn_mva=0.1, control_q=False)
        PV_2 = RES('PV 2', source='SOLAR', bus='Bus 250', sn_mva=0.1, control_q=False)
        PV_3 = RES('PV 3', source='SOLAR', bus='Bus 43',  sn_mva=0.1, control_q=False)
        PV_4 = RES('PV 4', source='SOLAR', bus='Bus 450', sn_mva=0.1, control_q=False)
        PV_5 = RES('PV 5', source='SOLAR', bus='Bus 39',  sn_mva=0.1, control_q=False)
        WP_1 = RES('WP_1', source='WIND', bus='Bus 4',  sn_mva=0.1, control_q=False)
        WP_2 = RES('WP_2', source='WIND', bus='Bus 59', sn_mva=0.1, control_q=False)
        WP_3 = RES('WP_3', source='WIND', bus='Bus 46', sn_mva=0.1, control_q=False)
        WP_4 = RES('WP_4', source='WIND', bus='Bus 75', sn_mva=0.1, control_q=False)
        WP_5 = RES('WP_5', source='WIND', bus='Bus 83', sn_mva=0.1, control_q=False)
        TAP_1 = Transformer('TAP 1', type='TAP', fbus='Bus 150', tbus='Bus 149', sn_mva=5., tap_max=2,  tap_min=-2)
        TAP_2 = Transformer('TAP 2', type='TAP', fbus='Bus 9',   tbus='Bus 14',  sn_mva=1., tap_max=16, tap_min=-16)
        TAP_3 = Transformer('TAP 3', type='TAP', fbus='Bus 25',  tbus='Bus 26',  sn_mva=1., tap_max=16, tap_min=-16)
        TAP_4 = Transformer('TAP 4', type='TAP', fbus='Bus 160', tbus='Bus 67',  sn_mva=1., tap_max=2, tap_min=-2)
        SCB_1 = Shunt('SCB 1', bus='Bus 108', q_mvar=-0.3, max_step=4)
        SCB_2 = Shunt('SCB 2', bus='Bus 76',  q_mvar=-0.3, max_step=4)
        ESS_1 = ESS('Storage 1', bus='Bus 20', min_p_mw=-0.5, max_p_mw=0.5, max_e_mwh=2, min_e_mwh=0.2)
        ESS_2 = ESS('Storage 2', bus='Bus 56', min_p_mw=-0.5, max_p_mw=0.5, max_e_mwh=2, min_e_mwh=0.2)
        # ESS_3 = ESS('Storage 3', bus='Bus 113', min_p_mw=-0.25, max_p_mw=0.25, max_e_mwh=1, min_e_mwh=0.1)
        GRID = Grid('GRID', bus='Bus 150', sn_mva=5.)
        SW_1 = Switch('SW 1', fbus='Bus 18', tbus='Bus 135')
        SW_2 = Switch('SW 2', fbus='Bus 13', tbus='Bus 152')
        SW_3 = Switch('SW 3', fbus='Bus 54', tbus='Bus 94')
        SW_4 = Switch('SW 4', fbus='Bus 60', tbus='Bus 160')
        SW_5 = Switch('SW 5', fbus='Bus 97', tbus='Bus 197')

        self.agents = [DG_1, DG_3, DG_4, PV_1, PV_2, PV_3, PV_4, PV_5, WP_1, WP_2, WP_3, WP_4, WP_5, \
            TAP_1, TAP_2, TAP_3, TAP_4, SCB_1, SCB_2, ESS_1, ESS_2, GRID, SW_1, SW_2, SW_3, SW_4, SW_5]

        # reset
        ob = self.reset()

        # configure spaces
        action_space, action_shape = [], 0
        for agent in self.policy_agents:
            total_action_space = []
            # continuous action space
            if agent.action.range is not None:
                low, high = agent.action.range
                u_action_space = gym.spaces.Box(low=low, high=high, dtype=np.float32)
                total_action_space.append(u_action_space)
                action_shape += u_action_space.shape[-1]
            # discrete action space
            if agent.action.ncats is not None:
                if isinstance(agent.action.ncats, list):
                    u_action_space = gym.spaces.MultiDiscrete(agent.action.ncats)
                    action_shape += u_action_space.nvec.shape[-1]
                elif isinstance(agent.action.ncats, int):
                    if agent.type == 'SCB':
                        u_action_space = gym.spaces.Box(low=np.array([0]), high=np.array([agent.max_step]), dtype=np.float32)
                    elif agent.type == 'TAP':
                        u_action_space = gym.spaces.Box(low=np.array([agent.tap_min]), high=np.array([agent.tap_max]), dtype=np.float32)
                    action_shape += 1
                else:
                    raise NotImplementedError()
                total_action_space.append(u_action_space)

            action_space.extend(total_action_space)

        low = np.concatenate([ac.low for ac in action_space])
        high = np.concatenate([ac.high for ac in action_space])
        self.action_space = gym.spaces.Box(low=low, high=high, dtype=np.float32)
        # observation space
        self.observation_space = gym.spaces.Box(low=-np.inf, high=+np.inf, shape=(ob.shape[0],), dtype=np.float32)

        # reward
        self.reward_range = (-200.0, 200.0)

    # return all agents controllable by external policies
    @property
    def policy_agents(self):
        return [agent for agent in self.agents if agent.action_callback is None]

    @property
    def scripted_agents(self):
        return [agent for agent in self.agents if agent.action_callback is not None]

    @property
    def resource_agents(self):
        return [agent for agent in self.agents if agent.type in ['GRID', 'DG', 'CL', 'ESS', 'SCB', 'SOLAR', 'WIND']]

    @property
    def grid_agent(self):
        return [agent for agent in self.agents if agent.type in ['GRID']]

    @property
    def dg_agents(self):
        return [agent for agent in self.agents if agent.type in ['DG']]

    @property
    def cl_agents(self):
        return [agent for agent in self.agents if agent.type in ['CL']]

    @property
    def res_agents(self):
        return [agent for agent in self.agents if agent.type in ['SOLAR', 'WIND']]

    @property
    def ess_agents(self):
        return [agent for agent in self.agents if agent.type in ['ESS']]

    @property
    def tap_agents(self):
        return [agent for agent in self.agents if agent.type in ['TAP']]

    @property
    def trafo_agents(self):
        return [agent for agent in self.agents if agent.type in ['Trafo']]

    @property
    def shunt_agents(self):
        return [agent for agent in self.agents if agent.type in ['SCB']]

    @property
    def switch_agents(self):
        return [agent for agent in self.agents if agent.type in ['SW']]

    def seed(self, seed=None):
        self.rnd, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        # set action for each agent
        self._set_action(action)
        # update agent state
        self._update_agent_state()
        # runpf
        net = self._update_net_state()
        # get reward
        reward, info = self._reward_and_safety(net)
        # update past observation
        self.past_load.append(self.dataset['load'][self.t])
        self.past_wind.append(self.dataset['wind'][self.t])
        self.past_solar.append(self.dataset['solar'][self.t])
        self.past_price.append(self.dataset['price_sigmoid'][self.t])
        # timestep counter
        self.t += 1
        if self.t >= self.total_timesteps:
            self.t = 0

        return self._get_obs(), reward, False, info

    # set env action for the agents
    def _set_action(self, action):
        s_index, t_index = 0, 0
        for agent in self.policy_agents:
            # continuous actions
            if agent.action.dim_c > 0:
                t_index += agent.action.dim_c
                agent.action.c = action[s_index:t_index]
                s_index = t_index
            # discrete actions
            if agent.action.dim_d > 0:
                t_index += agent.action.dim_d
                agent.action.d = action[s_index:t_index].round()
                s_index = t_index
        # make sure we used all elements of action
        assert s_index == t_index
        assert t_index == len(action)

    def _update_agent_state(self):
        for agent in self.agents:
            # set communication state (directly for now)
            if agent.type in ['DG', 'CL']:
                agent.update_state()
            elif agent.type == 'ESS':
                agent.update_state()
            elif agent.type == 'SOLAR':
                agent.update_state(self.dataset['solar'][self.t])
            elif agent.type == 'WIND':
                agent.update_state(self.dataset['wind'][self.t])
            elif agent.type in ['TAP', 'Trafo']:
                agent.update_state()
            elif agent.type in ['SCB']:
                agent.update_state()
            elif agent.type in ['SW']:
                agent.update_state()
            else:
                pass

    def _update_net_state(self):
        net = self.net
        # update load info at all buses
        net.load.scaling = self.dataset['load'][self.t]
        # update sgen info at all buese
        net.sgen.p_mw = [agent.state.P for agent in self.dg_agents + self.res_agents]
        net.sgen.q_mvar = [agent.state.Q for agent in self.dg_agents + self.res_agents]
        net.shunt.step = [agent.state.step for agent in self.shunt_agents]
        net.storage.p_mw = [agent.state.P for agent in self.ess_agents]
        if self.topology == 'varying':
            if np.random.rand < 0.05:
                net.switch.closed = True
                opening_switch_id = np.random.choice(len(self.switch_agents))
                net.switch.closed[opening_switch_id] = False
                for closed, agent in zip(net.switch.closed.values, self.switch_agents):
                    agent.state.closed = closed
        # # update trafo info
        net.trafo.tap_pos[:len(self.tap_agents)] = [agent.state.tap_position for agent in self.tap_agents]
        # runpf
        try:
            pp.runpp(net) if self.AC else pp.rundcpp(net)
            # update grid state
            for agent in self.grid_agent:
                pgrid = net.res_ext_grid.p_mw.values[0]
                qgrid = net.res_ext_grid.q_mvar.values[0]
                agent.update_state(self.dataset['price'][self.t], pgrid, qgrid)
            # update transormers/voltage regulators cost and safety
            for agent in self.trafo_agents+self.tap_agents:
                agent.update_cost_safety(net.res_trafo.iloc[0].loading_percent)
            # update resource agents' cost and safety
            for agent in self.resource_agents:
                agent.update_cost_safety()
                assert agent.cost is not np.nan
                assert agent.safety is not np.nan
        except:
            pass

        return net

    def _reward_and_safety(self, net):
        if net["converged"]:
            # reward and safety
            reward, safety = 0, 0
            for agent in self.agents:
                reward -= agent.cost
                safety += agent.safety
            # update power flow safety
            vm = net.res_bus.vm_pu.values
            loading = net.res_line.loading_percent.values
            overloading = np.maximum(loading - 100, 0).sum()
            overvoltage = np.maximum(vm - 1.05, 0).sum()
            undervoltage = np.maximum(0.95 - vm, 0).sum()
            safety += overloading / 100 + overvoltage + undervoltage
        else:
            reward = -200.0
            safety = 2.0
            vm, loading = np.nan, np.nan
            print('Doesn\'t converge!')

        if self.kwargs.get('penalty_coef'):
            reward -= safety * self.kwargs.get('penalty_coef')
        if self.kwargs.get('safety_scale'):
            safety *= self.kwargs.get('safety_scale')
        # info
        info = {'s': safety}
        info['load'] = net.res_load.p_mw.sum()
        info['loading'] = loading
        info['voltage'] = vm
        
        return reward, info

    def reset(self, day=None, seed=None):
        # which day
        if day is None:
            day = self.rnd.randint(self.total_days-1)
        else:
            self.day = day
        # which hour
        self.t = day * 24
        # reset all agents
        if seed is not None:
            self.rnd, seed = seeding.np_random(seed)
        if self.train:
            for agent in self.agents:
                agent.reset(self.rnd)

        t, w, dataset = self.t, self.window, self.dataset
        if t-w >= 0:
            self.past_load = deque(dataset['load'][t-w:t], maxlen=w)
            self.past_wind = deque(dataset['wind'][t-w:t], maxlen=w)
            self.past_solar = deque(dataset['solar'][t-w:t], maxlen=w)
            self.past_price = deque(dataset['price_sigmoid'][t-w:t], maxlen=w)
        else:
            self.past_load = deque(np.hstack([dataset['load'][t-w:], dataset['load'][:t]]), maxlen=w)
            self.past_wind = deque(np.hstack([dataset['wind'][t-w:], dataset['wind'][:t]]), maxlen=w)
            self.past_solar = deque(np.hstack([dataset['solar'][t-w:], dataset['solar'][:t]]), maxlen=w)
            self.past_price = deque(np.hstack([dataset['price_sigmoid'][t-w:], dataset['price_sigmoid'][:t]]), maxlen=w)

        return self._get_obs()

    def _get_obs(self):
        internal_state = []
        internal_state.append((self.t%24) / 24.)
        for agent in self.ess_agents:
            internal_state.append(agent.state.soc)
        if self.topology == 'varying':
            for agent in self.switch_agents:
                internal_state.append(~agent.state.closed)
        internal_state = np.stack(internal_state).astype('float32')

        external_state = np.hstack([
            np.array(self.past_solar),
            np.array(self.past_wind),
            np.array(self.past_load),
            np.array(self.past_price),
        ])

        return np.hstack([internal_state, external_state]).astype('float32')
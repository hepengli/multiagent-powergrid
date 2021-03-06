from gym.envs.registration import register
from .ieee34 import IEEE34BusSystem
from .ieee123 import IEEE123BusSystem
from .ieee123_ddpg import IEEE123BusSystemDDPG
# from systems.environment_ieee34_ddpg import Environment_IEEE34_DDPG
# from systems.environment_cigre_mv import Environment_CIGRE_MV
# from systems.environment_cigre_lv import Environment_CIGRE_LV

# Multiagent Microgrid envs
# ----------------------------------------

register(
    id='ieee34-v0',
    entry_point='multiagent_powergrid.ieee34:IEEE34BusSystem',
    max_episode_steps=24,
)
register(
    id='ieee123-v0',
    entry_point='multiagent_powergrid.ieee123:IEEE123BusSystem',
    max_episode_steps=24,
)
register(
    id='ieee123ddpg-v0',
    entry_point='multiagent_powergrid.ieee123_ddpg:IEEE123BusSystemDDPG',
    max_episode_steps=24,
)
# register(
#     id='ieee34ddpg-v0',
#     entry_point='systems:Environment_IEEE34_DDPG',
#     max_episode_steps=24,
# )
# register(
#     id='CIGRE_MV-v0',
#     entry_point='systems:Environment_CIGRE_MV',
#     max_episode_steps=24,
# )
# register(
#     id='CIGRE_LV-v0',
#     entry_point='systems:Environment_CIGRE_LV',
#     max_episode_steps=24,
# )


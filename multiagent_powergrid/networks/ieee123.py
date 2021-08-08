from pandas import read_json
from numpy import nan
import pandapower as pp
try:
    import pplog as logging
except ImportError:
    import logging
logger = logging.getLogger(__name__)

def IEEE123Bus():
    """
    Create the IEEE 34 bus from IEEE PES Test Feeders:
    "https://site.ieee.org/pes-testfeeders/resources/”.

    OUTPUT:
        **net** - The pandapower format network.
    """
    net = pp.create_empty_network()

    # Linedata
    # CF-1
    line_data = {'c_nf_per_km': 4.2976310, 'r_ohm_per_km': 0.1901810,
                 'x_ohm_per_km': 0.3896204, 
                 'c0_nf_per_km': 2.0019129, 'r0_ohm_per_km': 0.4806720,
                 'x0_ohm_per_km': 1.2037409, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-1', element='line')

    # CF-2
    line_data = {'c_nf_per_km': 4.2976310, 'r_ohm_per_km': 0.1901810,
                 'x_ohm_per_km': 0.3896204, 
                 'c0_nf_per_km': 2.0019129, 'r0_ohm_per_km': 0.4806720,
                 'x0_ohm_per_km': 1.2037409, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-2', element='line')

    # CF-3
    line_data = {'c_nf_per_km': 4.2976310, 'r_ohm_per_km': 0.1901810,
                 'x_ohm_per_km': 0.3896204, 
                 'c0_nf_per_km': 2.0019129, 'r0_ohm_per_km': 0.4806720,
                 'x0_ohm_per_km': 1.2037409, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-3', element='line')

    # CF-4
    line_data = {'c_nf_per_km': 4.2976310, 'r_ohm_per_km': 0.1901810,
                 'x_ohm_per_km': 0.3896204, 
                 'c0_nf_per_km': 2.0019129, 'r0_ohm_per_km': 0.4806720,
                 'x0_ohm_per_km': 1.2037409, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-4', element='line')

    # CF-5
    line_data = {'c_nf_per_km': 4.2976310, 'r_ohm_per_km': 0.1901810,
                 'x_ohm_per_km': 0.3896204, 
                 'c0_nf_per_km': 2.0019129, 'r0_ohm_per_km': 0.4806720,
                 'x0_ohm_per_km': 1.2037409, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-5', element='line')

    # CF-6
    line_data = {'c_nf_per_km': 4.2976310, 'r_ohm_per_km': 0.1901810,
                 'x_ohm_per_km': 0.3896204, 
                 'c0_nf_per_km': 2.0019129, 'r0_ohm_per_km': 0.4806720,
                 'x0_ohm_per_km': 1.2037409, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-6', element='line')

    # CF-7
    line_data = {'c_nf_per_km': 2.3489280, 'r_ohm_per_km': 0.15857392,
                 'x_ohm_per_km': 0.3641649, 
                 'c0_nf_per_km': 1.6934436, 'r0_ohm_per_km': 0.2539544,
                 'x0_ohm_per_km': 0.6033307, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-7', element='line')

    # CF-8
    line_data = {'c_nf_per_km': 2.3489280, 'r_ohm_per_km': 0.15857392,
                 'x_ohm_per_km': 0.3641649, 
                 'c0_nf_per_km': 1.6934436, 'r0_ohm_per_km': 0.2539544,
                 'x0_ohm_per_km': 0.6033307, 
                 'max_i_ka': 0.53, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-8', element='line')

    # CF-9
    line_data = {'c_nf_per_km': 0.9360542, 'r_ohm_per_km': 0.2753088,
                 'x_ohm_per_km': 0.2790992, 
                 'c0_nf_per_km': 0.9360542, 'r0_ohm_per_km': 0.2753088,
                 'x0_ohm_per_km': 0.2790992, 
                 'max_i_ka': 0.23, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-9', element='line')

    # CF-10
    line_data = {'c_nf_per_km': 0.9360542, 'r_ohm_per_km': 0.2753088,
                 'x_ohm_per_km': 0.2790992, 
                 'c0_nf_per_km': 0.9360542, 'r0_ohm_per_km': 0.2753088,
                 'x0_ohm_per_km': 0.2790992, 
                 'max_i_ka': 0.23, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-10', element='line')

    # CF-11
    line_data = {'c_nf_per_km': 0.9360542, 'r_ohm_per_km': 0.2753088,
                 'x_ohm_per_km': 0.2790992, 
                 'c0_nf_per_km': 0.9360542, 'r0_ohm_per_km': 0.2753088,
                 'x0_ohm_per_km': 0.2790992, 
                 'max_i_ka': 0.23, 'type': 'ol'}
    pp.create_std_type(net, line_data, name='CF-11', element='line')

    # CF-12
    line_data = {'c_nf_per_km': 41.7711813, 'r_ohm_per_km': 0.6302153,
                 'x_ohm_per_km': 0.3002672, 
                 'c0_nf_per_km': 41.7711813, 'r0_ohm_per_km': 1.5821560,
                 'x0_ohm_per_km': 0.7791580, 
                 'max_i_ka': 0.31, 'type': 'cs'}
    pp.create_std_type(net, line_data, name='CF-12', element='line')

    # Busses
    bus_1   = pp.create_bus(net, name='Bus 1',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_2   = pp.create_bus(net, name='Bus 2',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_3   = pp.create_bus(net, name='Bus 3',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_4   = pp.create_bus(net, name='Bus 4',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_5   = pp.create_bus(net, name='Bus 5',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_6   = pp.create_bus(net, name='Bus 6',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_7   = pp.create_bus(net, name='Bus 7',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_8   = pp.create_bus(net, name='Bus 8',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_9   = pp.create_bus(net, name='Bus 9',   vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_10  = pp.create_bus(net, name='Bus 10',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_11  = pp.create_bus(net, name='Bus 11',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_12  = pp.create_bus(net, name='Bus 12',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_13  = pp.create_bus(net, name='Bus 13',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_14  = pp.create_bus(net, name='Bus 14',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_15  = pp.create_bus(net, name='Bus 15',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_16  = pp.create_bus(net, name='Bus 16',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_17  = pp.create_bus(net, name='Bus 17',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_18  = pp.create_bus(net, name='Bus 18',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_19  = pp.create_bus(net, name='Bus 19',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_20  = pp.create_bus(net, name='Bus 20',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_21  = pp.create_bus(net, name='Bus 21',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_22  = pp.create_bus(net, name='Bus 22',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_23  = pp.create_bus(net, name='Bus 23',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_24  = pp.create_bus(net, name='Bus 24',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_25  = pp.create_bus(net, name='Bus 25',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_26  = pp.create_bus(net, name='Bus 26',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_27  = pp.create_bus(net, name='Bus 27',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_28  = pp.create_bus(net, name='Bus 28',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_29  = pp.create_bus(net, name='Bus 29',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_30  = pp.create_bus(net, name='Bus 30',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_31  = pp.create_bus(net, name='Bus 31',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_32  = pp.create_bus(net, name='Bus 32',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_33  = pp.create_bus(net, name='Bus 33',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_34  = pp.create_bus(net, name='Bus 34',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_35  = pp.create_bus(net, name='Bus 35',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_36  = pp.create_bus(net, name='Bus 36',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_37  = pp.create_bus(net, name='Bus 37',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_38  = pp.create_bus(net, name='Bus 38',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_39  = pp.create_bus(net, name='Bus 39',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_40  = pp.create_bus(net, name='Bus 40',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_41  = pp.create_bus(net, name='Bus 41',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_42  = pp.create_bus(net, name='Bus 42',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_43  = pp.create_bus(net, name='Bus 43',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_44  = pp.create_bus(net, name='Bus 44',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_45  = pp.create_bus(net, name='Bus 45',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_46  = pp.create_bus(net, name='Bus 46',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_47  = pp.create_bus(net, name='Bus 47',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_48  = pp.create_bus(net, name='Bus 48',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_49  = pp.create_bus(net, name='Bus 49',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_50  = pp.create_bus(net, name='Bus 50',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_51  = pp.create_bus(net, name='Bus 51',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_52  = pp.create_bus(net, name='Bus 52',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_53  = pp.create_bus(net, name='Bus 53',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_54  = pp.create_bus(net, name='Bus 54',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_55  = pp.create_bus(net, name='Bus 55',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_56  = pp.create_bus(net, name='Bus 56',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_57  = pp.create_bus(net, name='Bus 57',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_58  = pp.create_bus(net, name='Bus 58',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_59  = pp.create_bus(net, name='Bus 59',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_60  = pp.create_bus(net, name='Bus 60',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_61  = pp.create_bus(net, name='Bus 61',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_62  = pp.create_bus(net, name='Bus 62',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_63  = pp.create_bus(net, name='Bus 63',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_64  = pp.create_bus(net, name='Bus 64',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_65  = pp.create_bus(net, name='Bus 65',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_66  = pp.create_bus(net, name='Bus 66',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_67  = pp.create_bus(net, name='Bus 67',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_68  = pp.create_bus(net, name='Bus 68',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_69  = pp.create_bus(net, name='Bus 69',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_70  = pp.create_bus(net, name='Bus 70',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_71  = pp.create_bus(net, name='Bus 71',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_72  = pp.create_bus(net, name='Bus 72',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_73  = pp.create_bus(net, name='Bus 73',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_74  = pp.create_bus(net, name='Bus 74',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_75  = pp.create_bus(net, name='Bus 75',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_76  = pp.create_bus(net, name='Bus 76',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_77  = pp.create_bus(net, name='Bus 77',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_78  = pp.create_bus(net, name='Bus 78',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_79  = pp.create_bus(net, name='Bus 79',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_80  = pp.create_bus(net, name='Bus 80',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_81  = pp.create_bus(net, name='Bus 81',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_82  = pp.create_bus(net, name='Bus 82',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_83  = pp.create_bus(net, name='Bus 83',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_84  = pp.create_bus(net, name='Bus 84',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_85  = pp.create_bus(net, name='Bus 85',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_86  = pp.create_bus(net, name='Bus 86',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_87  = pp.create_bus(net, name='Bus 87',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_88  = pp.create_bus(net, name='Bus 88',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_89  = pp.create_bus(net, name='Bus 89',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_90  = pp.create_bus(net, name='Bus 90',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_91  = pp.create_bus(net, name='Bus 91',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_92  = pp.create_bus(net, name='Bus 92',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_93  = pp.create_bus(net, name='Bus 93',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_94  = pp.create_bus(net, name='Bus 94',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_95  = pp.create_bus(net, name='Bus 95',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_96  = pp.create_bus(net, name='Bus 96',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_97  = pp.create_bus(net, name='Bus 97',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_98  = pp.create_bus(net, name='Bus 98',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_99  = pp.create_bus(net, name='Bus 99',  vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_100 = pp.create_bus(net, name='Bus 100', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_101 = pp.create_bus(net, name='Bus 101', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_102 = pp.create_bus(net, name='Bus 102', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_103 = pp.create_bus(net, name='Bus 103', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_104 = pp.create_bus(net, name='Bus 104', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_105 = pp.create_bus(net, name='Bus 105', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_106 = pp.create_bus(net, name='Bus 106', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_107 = pp.create_bus(net, name='Bus 107', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_108 = pp.create_bus(net, name='Bus 108', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_109 = pp.create_bus(net, name='Bus 109', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_110 = pp.create_bus(net, name='Bus 110', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_111 = pp.create_bus(net, name='Bus 111', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_112 = pp.create_bus(net, name='Bus 112', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_113 = pp.create_bus(net, name='Bus 113', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_114 = pp.create_bus(net, name='Bus 114', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_135 = pp.create_bus(net, name='Bus 135', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_149 = pp.create_bus(net, name='Bus 149', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_152 = pp.create_bus(net, name='Bus 152', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_160 = pp.create_bus(net, name='Bus 160', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_197 = pp.create_bus(net, name='Bus 197', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_250 = pp.create_bus(net, name='Bus 250', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_300 = pp.create_bus(net, name='Bus 300', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_450 = pp.create_bus(net, name='Bus 450', vn_kv=4.16, type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)
    bus_150 = pp.create_bus(net, name='Bus 150', vn_kv=115., type='b', zone='123_BUS', max_vm_pu=1.05, min_vm_pu=0.95)

    # Lines
    pp.create_line(net, bus_149, bus_1,   length_km=0.12192, std_type='CF-1',  name='Line 1')
    pp.create_line(net, bus_1,   bus_2,   length_km=0.05334, std_type='CF-10', name='Line 2')
    pp.create_line(net, bus_1,   bus_3,   length_km=0.07620, std_type='CF-11', name='Line 3')
    pp.create_line(net, bus_1,   bus_7,   length_km=0.09144, std_type='CF-1',  name='Line 4')
    pp.create_line(net, bus_3,   bus_4,   length_km=0.06096, std_type='CF-11', name='Line 5')
    pp.create_line(net, bus_3,   bus_5,   length_km=0.09906, std_type='CF-11', name='Line 6')
    pp.create_line(net, bus_5,   bus_6,   length_km=0.07620, std_type='CF-11', name='Line 7')
    pp.create_line(net, bus_7,   bus_8,   length_km=0.06096, std_type='CF-1',  name='Line 8')
    pp.create_line(net, bus_8,   bus_12,  length_km=0.06858, std_type='CF-10', name='Line 9')
    pp.create_line(net, bus_8,   bus_9,   length_km=0.06858, std_type='CF-9',  name='Line 10')
    pp.create_line(net, bus_8,   bus_13,  length_km=0.09144, std_type='CF-1',  name='Line 11')
    # pp.create_line(net, bus_9,   bus_14,  length_km=0.12954, std_type='CF-9',  name='Line 12')
    pp.create_line(net, bus_13,  bus_34,  length_km=0.04572, std_type='CF-11', name='Line 13')
    pp.create_line(net, bus_13,  bus_18,  length_km=0.25146, std_type='CF-2',  name='Line 14')
    pp.create_line(net, bus_14,  bus_11,  length_km=0.07620, std_type='CF-9',  name='Line 15')
    pp.create_line(net, bus_14,  bus_10,  length_km=0.07620, std_type='CF-9',  name='Line 16')
    pp.create_line(net, bus_15,  bus_16,  length_km=0.11430, std_type='CF-11', name='Line 17')
    pp.create_line(net, bus_15,  bus_17,  length_km=0.10668, std_type='CF-11', name='Line 18')
    pp.create_line(net, bus_18,  bus_19,  length_km=0.07620, std_type='CF-9',  name='Line 19')
    pp.create_line(net, bus_18,  bus_21,  length_km=0.09144, std_type='CF-2',  name='Line 20')
    pp.create_line(net, bus_19,  bus_20,  length_km=0.09906, std_type='CF-9',  name='Line 21')
    pp.create_line(net, bus_21,  bus_22,  length_km=0.16002, std_type='CF-10', name='Line 22')
    pp.create_line(net, bus_21,  bus_23,  length_km=0.07620, std_type='CF-2',  name='Line 23')
    pp.create_line(net, bus_23,  bus_24,  length_km=0.15240, std_type='CF-11', name='Line 24')
    pp.create_line(net, bus_23,  bus_25,  length_km=0.08382, std_type='CF-2',  name='Line 25')
    # pp.create_line(net, bus_25,  bus_26,  length_km=0.10668, std_type='CF-7',  name='Line 26')
    pp.create_line(net, bus_25,  bus_28,  length_km=0.06096, std_type='CF-2',  name='Line 27')
    pp.create_line(net, bus_26,  bus_27,  length_km=0.08382, std_type='CF-7',  name='Line 28')
    pp.create_line(net, bus_26,  bus_31,  length_km=0.06858, std_type='CF-11', name='Line 29')
    pp.create_line(net, bus_27,  bus_33,  length_km=0.15240, std_type='CF-9',  name='Line 30')
    pp.create_line(net, bus_28,  bus_29,  length_km=0.09144, std_type='CF-2',  name='Line 31')
    pp.create_line(net, bus_29,  bus_30,  length_km=0.10668, std_type='CF-2',  name='Line 32')
    pp.create_line(net, bus_30,  bus_250, length_km=0.06096, std_type='CF-2',  name='Line 33')
    pp.create_line(net, bus_31,  bus_32,  length_km=0.15240, std_type='CF-11', name='Line 34')
    pp.create_line(net, bus_34,  bus_15,  length_km=0.08382, std_type='CF-11', name='Line 35')
    pp.create_line(net, bus_35,  bus_36,  length_km=0.10668, std_type='CF-8',  name='Line 36')
    pp.create_line(net, bus_35,  bus_40,  length_km=0.06096, std_type='CF-1',  name='Line 37')
    pp.create_line(net, bus_36,  bus_37,  length_km=0.08382, std_type='CF-9',  name='Line 38')
    pp.create_line(net, bus_36,  bus_38,  length_km=0.06858, std_type='CF-10', name='Line 39')
    pp.create_line(net, bus_38,  bus_39,  length_km=0.15240, std_type='CF-10', name='Line 40')
    pp.create_line(net, bus_40,  bus_41,  length_km=0.09144, std_type='CF-11', name='Line 41')
    pp.create_line(net, bus_40,  bus_42,  length_km=0.10668, std_type='CF-1',  name='Line 42')
    pp.create_line(net, bus_42,  bus_43,  length_km=0.06096, std_type='CF-10', name='Line 43')
    pp.create_line(net, bus_42,  bus_44,  length_km=0.06096, std_type='CF-1',  name='Line 44')
    pp.create_line(net, bus_44,  bus_45,  length_km=0.06096, std_type='CF-9',  name='Line 45')
    pp.create_line(net, bus_44,  bus_47,  length_km=0.07620, std_type='CF-1',  name='Line 46')
    pp.create_line(net, bus_45,  bus_46,  length_km=0.09144, std_type='CF-9',  name='Line 47')
    pp.create_line(net, bus_47,  bus_48,  length_km=0.04572, std_type='CF-4',  name='Line 48')
    pp.create_line(net, bus_47,  bus_49,  length_km=0.07620, std_type='CF-4',  name='Line 49')
    pp.create_line(net, bus_49,  bus_50,  length_km=0.07620, std_type='CF-4',  name='Line 50')
    pp.create_line(net, bus_50,  bus_51,  length_km=0.07620, std_type='CF-4',  name='Line 51')
    pp.create_line(net, bus_52,  bus_53,  length_km=0.06096, std_type='CF-1',  name='Line 52')
    pp.create_line(net, bus_53,  bus_54,  length_km=0.03810, std_type='CF-1',  name='Line 53')
    pp.create_line(net, bus_54,  bus_55,  length_km=0.08382, std_type='CF-1',  name='Line 54')
    pp.create_line(net, bus_54,  bus_57,  length_km=0.10668, std_type='CF-3',  name='Line 55')
    pp.create_line(net, bus_55,  bus_56,  length_km=0.08382, std_type='CF-1',  name='Line 56')
    pp.create_line(net, bus_57,  bus_58,  length_km=0.07620, std_type='CF-10', name='Line 57')
    pp.create_line(net, bus_57,  bus_60,  length_km=0.22860, std_type='CF-3',  name='Line 58')
    pp.create_line(net, bus_58,  bus_59,  length_km=0.07620, std_type='CF-10', name='Line 59')
    pp.create_line(net, bus_60,  bus_61,  length_km=0.16764, std_type='CF-5',  name='Line 60')
    pp.create_line(net, bus_60,  bus_62,  length_km=0.07620, std_type='CF-12', name='Line 61')
    pp.create_line(net, bus_62,  bus_63,  length_km=0.05334, std_type='CF-12', name='Line 62')
    pp.create_line(net, bus_63,  bus_64,  length_km=0.10668, std_type='CF-12', name='Line 63')
    pp.create_line(net, bus_64,  bus_65,  length_km=0.12954, std_type='CF-12', name='Line 64')
    pp.create_line(net, bus_65,  bus_66,  length_km=0.09906, std_type='CF-12', name='Line 65')
    pp.create_line(net, bus_67,  bus_68,  length_km=0.06096, std_type='CF-9',  name='Line 66')
    pp.create_line(net, bus_67,  bus_72,  length_km=0.08382, std_type='CF-3',  name='Line 67')
    pp.create_line(net, bus_67,  bus_97,  length_km=0.07620, std_type='CF-3',  name='Line 68')
    pp.create_line(net, bus_68,  bus_69,  length_km=0.08382, std_type='CF-9',  name='Line 69')
    pp.create_line(net, bus_69,  bus_70,  length_km=0.09906, std_type='CF-9',  name='Line 69')
    pp.create_line(net, bus_70,  bus_71,  length_km=0.08382, std_type='CF-9',  name='Line 70')
    pp.create_line(net, bus_72,  bus_73,  length_km=0.08382, std_type='CF-11', name='Line 71')
    pp.create_line(net, bus_72,  bus_76,  length_km=0.06096, std_type='CF-3',  name='Line 72')
    pp.create_line(net, bus_73,  bus_74,  length_km=0.10668, std_type='CF-11', name='Line 73')
    pp.create_line(net, bus_74,  bus_75,  length_km=0.12192, std_type='CF-11', name='Line 74')
    pp.create_line(net, bus_76,  bus_77,  length_km=0.12192, std_type='CF-6',  name='Line 75')
    pp.create_line(net, bus_76,  bus_86,  length_km=0.21336, std_type='CF-3',  name='Line 76')
    pp.create_line(net, bus_77,  bus_78,  length_km=0.03048, std_type='CF-6',  name='Line 77')
    pp.create_line(net, bus_78,  bus_79,  length_km=0.06858, std_type='CF-6',  name='Line 78')
    pp.create_line(net, bus_78,  bus_80,  length_km=0.14478, std_type='CF-6',  name='Line 79')
    pp.create_line(net, bus_80,  bus_81,  length_km=0.14478, std_type='CF-6',  name='Line 80')
    pp.create_line(net, bus_81,  bus_82,  length_km=0.07620, std_type='CF-6',  name='Line 81')
    pp.create_line(net, bus_81,  bus_84,  length_km=0.20574, std_type='CF-11', name='Line 82')
    pp.create_line(net, bus_82,  bus_83,  length_km=0.07620, std_type='CF-6',  name='Line 83')
    pp.create_line(net, bus_84,  bus_85,  length_km=0.14478, std_type='CF-11', name='Line 84')
    pp.create_line(net, bus_86,  bus_87,  length_km=0.13716, std_type='CF-6',  name='Line 85')
    pp.create_line(net, bus_87,  bus_88,  length_km=0.05334, std_type='CF-9',  name='Line 86')
    pp.create_line(net, bus_87,  bus_89,  length_km=0.08382, std_type='CF-6',  name='Line 87')
    pp.create_line(net, bus_89,  bus_90,  length_km=0.06858, std_type='CF-10', name='Line 88')
    pp.create_line(net, bus_89,  bus_91,  length_km=0.06858, std_type='CF-6',  name='Line 89')
    pp.create_line(net, bus_91,  bus_92,  length_km=0.09144, std_type='CF-11', name='Line 90')
    pp.create_line(net, bus_91,  bus_93,  length_km=0.06858, std_type='CF-6',  name='Line 91')
    pp.create_line(net, bus_93,  bus_94,  length_km=0.08382, std_type='CF-9',  name='Line 92')
    pp.create_line(net, bus_93,  bus_95,  length_km=0.09144, std_type='CF-6',  name='Line 93')
    pp.create_line(net, bus_95,  bus_96,  length_km=0.06096, std_type='CF-10', name='Line 94')
    pp.create_line(net, bus_97,  bus_98,  length_km=0.08382, std_type='CF-3',  name='Line 95')
    pp.create_line(net, bus_98,  bus_99,  length_km=0.16764, std_type='CF-3',  name='Line 96')
    pp.create_line(net, bus_99,  bus_100, length_km=0.09144, std_type='CF-3',  name='Line 97')
    pp.create_line(net, bus_100, bus_450, length_km=0.24384, std_type='CF-3',  name='Line 98')
    pp.create_line(net, bus_101, bus_102, length_km=0.06858, std_type='CF-11', name='Line 99')
    pp.create_line(net, bus_101, bus_105, length_km=0.08382, std_type='CF-3',  name='Line 100')
    pp.create_line(net, bus_102, bus_103, length_km=0.09906, std_type='CF-11', name='Line 101')
    pp.create_line(net, bus_103, bus_104, length_km=0.21336, std_type='CF-11', name='Line 102')
    pp.create_line(net, bus_105, bus_106, length_km=0.06858, std_type='CF-10', name='Line 103')
    pp.create_line(net, bus_105, bus_108, length_km=0.09906, std_type='CF-3',  name='Line 104')
    pp.create_line(net, bus_106, bus_107, length_km=0.17526, std_type='CF-10', name='Line 105')
    pp.create_line(net, bus_108, bus_109, length_km=0.13716, std_type='CF-9',  name='Line 106')
    pp.create_line(net, bus_108, bus_300, length_km=0.30480, std_type='CF-3',  name='Line 107')
    pp.create_line(net, bus_109, bus_110, length_km=0.09144, std_type='CF-9',  name='Line 108')
    pp.create_line(net, bus_110, bus_111, length_km=0.17526, std_type='CF-9',  name='Line 109')
    pp.create_line(net, bus_110, bus_112, length_km=0.03810, std_type='CF-9',  name='Line 110')
    pp.create_line(net, bus_112, bus_113, length_km=0.16002, std_type='CF-9',  name='Line 111')
    pp.create_line(net, bus_113, bus_114, length_km=0.09906, std_type='CF-9',  name='Line 112')
    pp.create_line(net, bus_135, bus_35,  length_km=0.11430, std_type='CF-4',  name='Line 113')
    pp.create_line(net, bus_149, bus_1,   length_km=0.12192, std_type='CF-1',  name='Line 114')
    pp.create_line(net, bus_152, bus_52,  length_km=0.12192, std_type='CF-1',  name='Line 115')
    # pp.create_line(net, bus_160, bus_67,  length_km=0.10668, std_type='CF-6',  name='Line 116')
    pp.create_line(net, bus_197, bus_101, length_km=0.07620, std_type='CF-3',  name='Line 117')
    pp.create_line(net, bus_51, bus_300, length_km=0.19812, std_type='CF-4',  name='Line 118')

    # Substation / Regulator 1
    pp.create_transformer_from_parameters(net, bus_150, bus_149, sn_mva=5., vn_hv_kv=115.,
                                            vn_lv_kv=4.16, vkr_percent=1.0, vk_percent=8.062257,
                                            pfe_kw=0.0, i0_percent=0.0, shift_degree=30.0,
                                            tap_side='lv', tap_neutral=0, tap_max=2, tap_min=-2, 
                                            tap_step_percent=2.5, tap_pos=0, tap_phase_shifter=False,
                                            name='Regulator 1')

    # Regulator 2
    pp.create_transformer_from_parameters(net, bus_9, bus_14, sn_mva=1., vn_hv_kv=4.16,
                                          vn_lv_kv=4.16, vkr_percent=3.566, vk_percent=5.0784,
                                          pfe_kw=0.0, i0_percent=0.0, shift_degree=0.0,
                                          tap_side='lv', tap_neutral=0, tap_max=16, tap_min=-16, 
                                          tap_step_percent=0.625, tap_pos=0, tap_phase_shifter=False,
                                          name='Regulator 2')

    # Regulator 3
    pp.create_transformer_from_parameters(net, bus_25, bus_26, sn_mva=1., vn_hv_kv=4.16,
                                          vn_lv_kv=4.16, vkr_percent=1.6916, vk_percent=4.2372,
                                          pfe_kw=0.0, i0_percent=0.0, shift_degree=0.0,
                                          tap_side='lv', tap_neutral=0, tap_max=16, tap_min=-16, 
                                          tap_step_percent=0.625, tap_pos=0, tap_phase_shifter=False,
                                          name='Regulator 3')

    # Regulator 4
    pp.create_transformer_from_parameters(net, bus_160, bus_67, sn_mva=1., vn_hv_kv=4.16,
                                          vn_lv_kv=4.16, vkr_percent=2.0288, vk_percent=4.6252,
                                          pfe_kw=0.0, i0_percent=0.0, shift_degree=0.0,
                                          tap_side='lv', tap_neutral=0, tap_max=2, tap_min=-2, 
                                          tap_step_percent=2.5, tap_pos=0, tap_phase_shifter=False,
                                          name='Regulator 4')

    # Loads
    pp.create_load(net, bus_1,   p_mw=0.040, q_mvar=0.020, name='Load 1')
    pp.create_load(net, bus_2,   p_mw=0.020, q_mvar=0.010, name='Load 2')
    pp.create_load(net, bus_4,   p_mw=0.040, q_mvar=0.020, name='Load 4')
    pp.create_load(net, bus_5,   p_mw=0.020, q_mvar=0.010, name='Load 5')
    pp.create_load(net, bus_6,   p_mw=0.040, q_mvar=0.020, name='Load 5')
    pp.create_load(net, bus_7,   p_mw=0.020, q_mvar=0.010, name='Load 7')
    pp.create_load(net, bus_9,   p_mw=0.040, q_mvar=0.020, name='Load 9')
    pp.create_load(net, bus_10,  p_mw=0.020, q_mvar=0.010, name='Load 10')
    pp.create_load(net, bus_11,  p_mw=0.040, q_mvar=0.020, name='Load 11')
    pp.create_load(net, bus_12,  p_mw=0.020, q_mvar=0.010, name='Load 12')
    pp.create_load(net, bus_16,  p_mw=0.040, q_mvar=0.020, name='Load 16')
    pp.create_load(net, bus_17,  p_mw=0.020, q_mvar=0.010, name='Load 17')
    pp.create_load(net, bus_19,  p_mw=0.040, q_mvar=0.020, name='Load 19')
    pp.create_load(net, bus_20,  p_mw=0.040, q_mvar=0.020, name='Load 20')
    pp.create_load(net, bus_22,  p_mw=0.040, q_mvar=0.020, name='Load 22')
    pp.create_load(net, bus_24,  p_mw=0.040, q_mvar=0.020, name='Load 24')
    pp.create_load(net, bus_28,  p_mw=0.040, q_mvar=0.020, name='Load 28')
    pp.create_load(net, bus_29,  p_mw=0.040, q_mvar=0.020, name='Load 29')
    pp.create_load(net, bus_30,  p_mw=0.040, q_mvar=0.020, name='Load 30')
    pp.create_load(net, bus_31,  p_mw=0.020, q_mvar=0.010, name='Load 31')
    pp.create_load(net, bus_32,  p_mw=0.020, q_mvar=0.010, name='Load 32')
    pp.create_load(net, bus_33,  p_mw=0.040, q_mvar=0.020, name='Load 33')
    pp.create_load(net, bus_34,  p_mw=0.040, q_mvar=0.020, name='Load 34')
    pp.create_load(net, bus_35,  p_mw=0.040, q_mvar=0.020, name='Load 35')
    pp.create_load(net, bus_37,  p_mw=0.040, q_mvar=0.020, name='Load 37')
    pp.create_load(net, bus_38,  p_mw=0.020, q_mvar=0.010, name='Load 38')
    pp.create_load(net, bus_39,  p_mw=0.020, q_mvar=0.010, name='Load 39')
    pp.create_load(net, bus_41,  p_mw=0.020, q_mvar=0.010, name='Load 41')
    pp.create_load(net, bus_42,  p_mw=0.020, q_mvar=0.010, name='Load 42')
    pp.create_load(net, bus_43,  p_mw=0.040, q_mvar=0.020, name='Load 43')
    pp.create_load(net, bus_45,  p_mw=0.020, q_mvar=0.010, name='Load 45')
    pp.create_load(net, bus_46,  p_mw=0.020, q_mvar=0.010, name='Load 46')
    pp.create_load(net, bus_47,  p_mw=0.105, q_mvar=0.075, name='Load 47')
    pp.create_load(net, bus_48,  p_mw=0.210, q_mvar=0.150, name='Load 48')
    pp.create_load(net, bus_49,  p_mw=0.140, q_mvar=0.095, name='Load 49')
    pp.create_load(net, bus_50,  p_mw=0.040, q_mvar=0.020, name='Load 50')
    pp.create_load(net, bus_51,  p_mw=0.020, q_mvar=0.010, name='Load 51')
    pp.create_load(net, bus_52,  p_mw=0.040, q_mvar=0.020, name='Load 52')
    pp.create_load(net, bus_53,  p_mw=0.040, q_mvar=0.020, name='Load 53')
    pp.create_load(net, bus_55,  p_mw=0.020, q_mvar=0.010, name='Load 55')
    pp.create_load(net, bus_56,  p_mw=0.020, q_mvar=0.010, name='Load 56')
    pp.create_load(net, bus_58,  p_mw=0.020, q_mvar=0.010, name='Load 58')
    pp.create_load(net, bus_59,  p_mw=0.020, q_mvar=0.010, name='Load 59')
    pp.create_load(net, bus_60,  p_mw=0.020, q_mvar=0.010, name='Load 60')
    pp.create_load(net, bus_62,  p_mw=0.040, q_mvar=0.020, name='Load 62')
    pp.create_load(net, bus_63,  p_mw=0.040, q_mvar=0.020, name='Load 63')
    pp.create_load(net, bus_64,  p_mw=0.075, q_mvar=0.035, name='Load 64')
    pp.create_load(net, bus_65,  p_mw=0.140, q_mvar=0.095, name='Load 65')
    pp.create_load(net, bus_66,  p_mw=0.075, q_mvar=0.035, name='Load 66')
    pp.create_load(net, bus_68,  p_mw=0.020, q_mvar=0.010, name='Load 68')
    pp.create_load(net, bus_69,  p_mw=0.040, q_mvar=0.020, name='Load 69')
    pp.create_load(net, bus_70,  p_mw=0.020, q_mvar=0.010, name='Load 70')
    pp.create_load(net, bus_71,  p_mw=0.040, q_mvar=0.020, name='Load 71')
    pp.create_load(net, bus_73,  p_mw=0.040, q_mvar=0.020, name='Load 73')
    pp.create_load(net, bus_74,  p_mw=0.040, q_mvar=0.020, name='Load 74')
    pp.create_load(net, bus_75,  p_mw=0.040, q_mvar=0.020, name='Load 75')
    pp.create_load(net, bus_76,  p_mw=0.245, q_mvar=0.180, name='Load 76')
    pp.create_load(net, bus_77,  p_mw=0.040, q_mvar=0.020, name='Load 77')
    pp.create_load(net, bus_79,  p_mw=0.040, q_mvar=0.020, name='Load 79')
    pp.create_load(net, bus_80,  p_mw=0.040, q_mvar=0.020, name='Load 80')
    pp.create_load(net, bus_82,  p_mw=0.040, q_mvar=0.020, name='Load 82')
    pp.create_load(net, bus_83,  p_mw=0.020, q_mvar=0.010, name='Load 83')
    pp.create_load(net, bus_84,  p_mw=0.020, q_mvar=0.010, name='Load 84')
    pp.create_load(net, bus_85,  p_mw=0.040, q_mvar=0.020, name='Load 85')
    pp.create_load(net, bus_86,  p_mw=0.020, q_mvar=0.010, name='Load 86')
    pp.create_load(net, bus_87,  p_mw=0.040, q_mvar=0.020, name='Load 87')
    pp.create_load(net, bus_88,  p_mw=0.040, q_mvar=0.020, name='Load 88')
    pp.create_load(net, bus_90,  p_mw=0.040, q_mvar=0.020, name='Load 90')
    pp.create_load(net, bus_92,  p_mw=0.040, q_mvar=0.020, name='Load 92')
    pp.create_load(net, bus_94,  p_mw=0.040, q_mvar=0.020, name='Load 94')
    pp.create_load(net, bus_95,  p_mw=0.020, q_mvar=0.010, name='Load 95')
    pp.create_load(net, bus_96,  p_mw=0.020, q_mvar=0.010, name='Load 96')
    pp.create_load(net, bus_98,  p_mw=0.040, q_mvar=0.020, name='Load 98')
    pp.create_load(net, bus_99,  p_mw=0.040, q_mvar=0.020, name='Load 99')
    pp.create_load(net, bus_100, p_mw=0.040, q_mvar=0.020, name='Load 100')
    pp.create_load(net, bus_102, p_mw=0.020, q_mvar=0.010, name='Load 102')
    pp.create_load(net, bus_103, p_mw=0.040, q_mvar=0.020, name='Load 103')
    pp.create_load(net, bus_104, p_mw=0.040, q_mvar=0.020, name='Load 104')
    pp.create_load(net, bus_106, p_mw=0.040, q_mvar=0.020, name='Load 106')
    pp.create_load(net, bus_107, p_mw=0.040, q_mvar=0.020, name='Load 107')
    pp.create_load(net, bus_109, p_mw=0.040, q_mvar=0.020, name='Load 109')
    pp.create_load(net, bus_111, p_mw=0.020, q_mvar=0.010, name='Load 111')
    pp.create_load(net, bus_112, p_mw=0.020, q_mvar=0.010, name='Load 112')
    pp.create_load(net, bus_113, p_mw=0.040, q_mvar=0.020, name='Load 113')
    pp.create_load(net, bus_114, p_mw=0.020, q_mvar=0.010, name='Load 114')

    # External grid
    pp.create_ext_grid(net, bus_150, vm_pu=1.0, va_degree=0.0, s_sc_max_mva=5.0,
                       s_sc_min_mva=-5.0, rx_max=1, rx_min=1, r0x0_max=1, x0x_max=1)

    # Switches
    pp.create_switch(net, bus=bus_18,  element=bus_135, et='b', type="LS", z_ohm=0.1)
    pp.create_switch(net, bus=bus_13,  element=bus_152, et='b', type="LS", z_ohm=0.1)
    pp.create_switch(net, bus=bus_54,  element=bus_94,  et='b', type="LS", z_ohm=0.1)
    pp.create_switch(net, bus=bus_60,  element=bus_160, et='b', type="LS", z_ohm=0.1)
    pp.create_switch(net, bus=bus_97,  element=bus_197, et='b', type="LS", z_ohm=0.1)

    # Distributed generators
    pp.create_sgen(net, bus_24,  p_mw=0., q_mvar=0., name='DG 1', max_p_mw=0.66, min_p_mw=0, max_q_mvar=0.5, min_q_mvar=0)
    # pp.create_sgen(net, bus_41,  p_mw=0., q_mvar=0., name='DG 2', max_p_mw=0.66, min_p_mw=0, max_q_mvar=0.5, min_q_mvar=0)
    pp.create_sgen(net, bus_94,  p_mw=0., q_mvar=0., name='DG 3', max_p_mw=0.50, min_p_mw=0, max_q_mvar=0.375, min_q_mvar=0)
    pp.create_sgen(net, bus_71,  p_mw=0., q_mvar=0., name='DG 4', max_p_mw=0.50, min_p_mw=0, max_q_mvar=0.375, min_q_mvar=0)
    # pp.create_sgen(net, bus_114, p_mw=0., q_mvar=0., name='DG 5', max_p_mw=0.40, min_p_mw=0, max_q_mvar=0.3, min_q_mvar=0)
    pp.create_sgen(net, bus_22,  p_mw=0., type='PV', name='PV 1', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_250, p_mw=0., type='PV', name='PV 2', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_43,  p_mw=0., type='PV', name='PV 3', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_450, p_mw=0., type='PV', name='PV 4', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_39,  p_mw=0., type='PV', name='PV 5', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_4,   p_mw=0., type='WP', name='WP 1', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_59,  p_mw=0., type='WP', name='WP 2', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_46,  p_mw=0., type='WP', name='WP 3', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_75,  p_mw=0., type='WP', name='WP 4', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)
    pp.create_sgen(net, bus_83,  p_mw=0., type='WP', name='WP 5', max_p_mw=0.1, min_p_mw=0, max_q_mvar=0, min_q_mvar=0)

    # Shunt capacity bank
    pp.create_shunt_as_capacitor(net, bus_108, q_mvar=-0.3, name='SCB 1', step=0, max_step=4, loss_factor=0.0)
    pp.create_shunt_as_capacitor(net, bus_76,  q_mvar=-0.3, name='SCB 2', step=0, max_step=4, loss_factor=0.0)

    # storage
    pp.create_storage(net, bus_20, p_mw=0.0, max_e_mwh=2, sn_mva=1.0, soc_percent=50, min_e_mwh=0.2, name='Storage 1')
    pp.create_storage(net, bus_56, p_mw=0.0, max_e_mwh=2, sn_mva=1.0, soc_percent=50, min_e_mwh=0.2, name='Storage 2')
    #pp.create_storage(net, bus_113, p_mw=0.0, max_e_mwh=1, sn_mva=1.0, soc_percent=50, min_e_mwh=0.1, name='Storage 3')

    return net

# net = IEEE123Bus()
# pp.runpp(net)
# print(net.res_bus)
# print(net.res_ext_grid)
# print(net.trafo)
# print(net.res_load['p_mw'].values.sum())

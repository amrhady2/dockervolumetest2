from pycomm3 import LogixDriver


def read_single0():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_EM_DI_00')

def read_single1():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_EM_DI_01')

def read_single2():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_EM_DI_02')

def read_single3():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_EM_DI_03')

def read_single4():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_EM_DI_04')

def read_singleAI0():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_P3_AI_00')

def read_singleAI1():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_P3_AI_01')

def read_singleAI2():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_P1_AI_02')

def read_singleAI3():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_P1_AI_03')


     

def TEMP_Scaled_Value():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('TEMP_Scaled_Value')
    
def read_singleAO0():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_P2_AO_00')
    
def read_singleAO1():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_P2_AO_01')
    

def read_singleO8():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('_IO_EM_DO_08')


def read_multiple():
    tags = ['_IO_EM_DI_00', '_IO_EM_DI_01', '_IO_EM_DI_02', '_IO_EM_DI_03', '_IO_EM_DI_04', '_IO_EM_DI_05',
             '_IO_EM_DI_06', '_IO_EM_DI_07', '_IO_EM_DI_08'
        , '_IO_P2_AI_00', '_IO_P2_AI_01', '_IO_EM_DO_00', '_IO_EM_DO_02', '_IO_EM_DO_03', '_IO_EM_DO_04'
        , '_IO_EM_DO_05', '_IO_EM_DO_06', '_IO_EM_DO_07', '_IO_EM_DO_08']

    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read(*tags)


def read_array():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('DINT_ARY1{5}')


def read_array_slice():
    with LogixDriver('v/10') as plc:
        return plc.read('DINT_ARY1[50]{5}')


def read_strings():
    with LogixDriver('192.168.254.226/10') as plc:
        return plc.read('STRING1', 'STRING_ARY1[2]{2}')


def read_udt():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('SimpleUDT1_1')


def read_timer():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.read('TIMER1')


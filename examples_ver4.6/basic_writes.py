from pycomm3 import LogixDriver


def write_single_setA(Position_SetpointA):
    with LogixDriver('192.168.254.198/10') as plc:
        print('write_single_Position_SetpointA: ..............start writing.................')
        return plc.write(('Position_SetpointA', Position_SetpointA))

def write_single_setB(Position_SetpointB):
    with LogixDriver('192.168.254.198/10') as plc:
        print('write_single_Position_SetpointB: ..............start writing.................')        
        return plc.write(('Position_SetpointB', Position_SetpointB))

def write_single2():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DI_02', 0))

def write_single3():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DI_03', 1))

def write_single4():
    with LogixDriver('192.168.254.198/10') as plc:
        #print('write_single4_IO_EM_DI_04: start writing')
        return plc.write(('_IO_EM_DI_04', 1))



def write_single5():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DI_05', 1))

def write_single6():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DI_06', 1))

def write_single7():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DI_07', 1))


def write_single00():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DO_00', 1))


def write_single07():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('_IO_EM_DO_07', 0))




def write_multiple():
    with LogixDriver('192.168.254.198/10') as plc:
        return plc.write(('REAL2', 25.2), ('STRING3', 'A test for writing to a string.'))


def write_structure():
    with LogixDriver('192.168.254.198/10') as plc:
        recipe_data = {
            'Enabled': True,
            'OpCodes': [10, 11, 4, 20, 6, 20, 6, 30, 5, 0],
            'Targets': [100, 500, 85, 5, 15, 10.5, 20, 0, 0, 0],
            'StepDescriptions': ['Set Water Temperature',
                                 'Heated Water',
                                 'Start Agitator',
                                 'Hand Add - Flavor Part 1',
                                 'Timed Mix',
                                 'Hand Add - Flavor Part 2',
                                 'Timed Mix',
                                 'Transfer to Storage Tank',
                                 'Disable Agitator',
                                 ''],
            'TargetUnits': ['°F', 'lbs', '%', 'gal', 'min', 'lbs', 'min', '', '', ''],
            'Name': 'Our Fictional Recipe',
        }

        plc.write(('Example_Recipe', recipe_data))

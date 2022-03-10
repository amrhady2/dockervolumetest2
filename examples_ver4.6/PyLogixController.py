import pylogix

from pylogix import PLC

from pycomm3 import LogixDriver

with LogixDriver('192.168.254.198') as plc:
    print(plc)
    print(plc.revision_major)
    print(plc._cip_path)
    print(plc.read('_IO_EM_DI_01'))

# with PLC() as comm:
#     comm.IPAddress = '192.168.254.198'
#     ret = comm.Read('Input0')
#     print(ret.TagName, ret.Value, ret.Status)
#     print(ret)

# comm = PLC()
# comm.IPAddress = '192.168.254.198'
# comm.ProcessorSlot = 1
#
# result = comm.Read('_IO_EM_DI_00')
#
# print(result)
#

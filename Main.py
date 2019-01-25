import visa
visa_dll = 'c:/windows/system32/visa64.dll'
tcp_addr = 'TCPIP0::localhost::hislip0::INSTR'

rm = visa.ResourceManager(visa_dll)

tcp_inst = rm.open_resource(tcp_addr)

print(tcp_inst.query('*IDN?'))


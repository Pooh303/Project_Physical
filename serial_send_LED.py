import serial.tools.list_ports
import time

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()

ports_list = []

for port in ports:
    ports_list.append(str(port))
    print(str(port))

val: str = '5'

for i in range(len(ports_list)):
    if ports_list[i].startswith(f'COM{val}'):
        port_var = f'COM{val}'
        print(port_var)

serial_inst.baudrate = 9600
serial_inst.port = port_var
serial_inst.open()

while True:
    time.sleep(1)
    command: str = "DETECTED"
    # command = command.upper()
    command = command.encode('utf-8')
    serial_inst.write(command)

    if command == 'EXIT':
        exit(0)
from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
    'secret': 'class123!',
}

connection = ConnectHandler(**device)

commands1 = [
    'interface loopback0',
    'ip address 10.1.1.1 255.255.255.0',
    'no shutdown',
    'exit'
]
output0 = connection.send_command('configure terminal')
output1 = connection.send_command('interface loopback0')
output2 = connection.send_command('ip address 10.1.1.1 255.255.255.0')
output3 = connection.send_command('no shutdown')

commands2 = [
    'interface GigabitEthernet2',
    'ip address 192.168.56.0 255.255.255.0',
    'no shutdown',
    'exit'
]
output4 = connection.send_command('configure terminal')
output5 = connection.send_command('configure terminal')
commands3 = [
    'router ospf 1',
    'network 10.1.1.0 0.0.0.255 area 0',
    'network 192.168.2.0 0.0.0.255 area 0',
    'exit'
]

#output1 = connection.send_command('show ip interface')

#output2 = connection.send_command('show ip interface')
#print (output2)

#output3 = connection.send_command('show ip interface')
#print (output3)

connection.disconnect()

from netmiko import ConnectHandler

# Device details
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.1',
    'username': 'cisco',
    'password': 'cisco123!',
    'secret': 'class123!'
}

# Connect to the device
connection = ConnectHandler(**device)

# Configure a loopback interface
commands1 = [
    'interface Loopback0',
    'ip address 10.1.1.1 255.255.255.0',
    'exit'
]

# Configure another interface
commands2 = [
    'interface GigabitEthernet0/0',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
    'exit'
]

# Configure OSPF routing protocol
commands3 = [
    'router ospf 1',
    'network 10.1.1.0 0.0.0.255 area 0',
    'network 192.168.2.0 0.0.0.255 area 0',
    'exit'
]


#output for commands 1 ,2,3
output1 = connection.sendconfig.set(commands1) 
print (output1)

output2 = connection.sendconfig.set(commands2) 
print (output2)

output3 = connection.sendconfig.set(commands3) 
print (output3)

# Disconnect from the device
connection.disconnect()
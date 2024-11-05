from netmiko import ConnectHandler
import difflib

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.56.101',
    'username': 'cisco',
    'password': 'cisco123!',
}

connection = ConnectHandler(**device)

running_config = connection.send_command('show running-config')
startup_config = connection.send_command('show startup-config')

with open('running_config.txt','w') as run_file:
    run_file.write(running_config)

with open('startup_config.txt','w') as start_file:
    start_file.write(startup_config)

diff = difflib.unified_diff(
    running_config.splitlines(),
    startup_config.splitlines(),
    fromfile='Running-config',
    tofile='Startup-config',
    lineterm=''
)

print('\n'.join(list(diff)))

connection.disconnect()

print("Configs retrieved and stored successfully.")
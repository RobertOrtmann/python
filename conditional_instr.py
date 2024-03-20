port_status = "up"
if port_status == "up":
    print("The port is operational.")

if port_status == "up" :
    print("The port is operational.")
else:
    print("The port is down.")

port_speed = 1000
if port_speed == 100:
    print("FastEthernet port.")
elif port_speed == 1000:
    print("GigabitEthernet port.")
else:
    print("Speed unrecognized.")

interface_configs = {
    "GigabitEthernet0/1" : {"status" : "up", "vlan" : "10"},
    "GigabitEthernet0/2" : {"status" : "down", "vlan" : "20"},
    "GigabitEthernet0/3" : {"status" : "up", "vlan" : "10"}
}

ip_addresses = ['192.168.1.1', '10.0.0.1', '172.16.0.1']
for ip in ip_addresses:
    print(ip)


command = "show ip interface brief"
for char in command:
    print(char)

interfaces = {'GigabitEthernet0' : 'up', 'GigabitEthernet1' : 'down' }
for interface, status in interfaces.items() :
    print(f"Interface {interface} is {status}")

for i in range(5) :
    print(f"Interface GigabitEthernet0/{i}")


counter = 0
while counter < 5:
    print(f"Counter is {counter}")
    counter += 1

counter = 0
while True:  # infinite loop
    if counter == 5:
        break # exit the loop
print(f"Counter is{counter}")
counter += 1

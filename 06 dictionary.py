device = {
    "hostname" : "Router1",
    "ip" : "192.168.1.1" ,
    "model" : "Cisco 2901" ,
    "interfaces" : ["GigabitEthernet0" , "GigabitEthernet1"]
}
print(device)

ip_address = device["ip"]
print(f"Device IP Address: {ip_address}")


device["location"] = "Data Center A"
print(device)

device["ip"] = "192.168.2.1"
print(device)

del device["model"] # using del
location = device.pop("location") # using pop, also retrieves the value
print(device)
print(location)

for key in device.keys():
    print(key)

for value in device.values():
    print(value)

for key, value in device.items():
    print(f"{key}: {value}")

routing_table = {
    "10.0.0.0./24" : "192.168.1.1" ,
    "172.16.0.0/16" : "192.168.2.1"
}
for network, next_hop in routing_table.items():
    print(f"Destination: {network}, next Hop: {next_hop}")




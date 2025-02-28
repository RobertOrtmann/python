port_status = "up"
if port_status == "up":
    print("The port is operational.")

port_status = "down"
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

# Define the VLAN to search for
vlan_to_check = input("Provide vlan to be checked:")

# Check each interface configuration
if interface_configs["GigabitEthernet0/1"]["vlan"] == vlan_to_check:
    print(f"VLAN {vlan_to_check} is assigned to interface GigabitEthernet0/1")
elif interface_configs["GigabitEthernet0/2"]["vlan"] == vlan_to_check:
    print(f"VLAN {vlan_to_check} is assigned to interface GigabitEthernet0/2")
elif interface_configs["GigabitEthernet0/3"]["vlan"] == vlan_to_check:
    print(f"VLAN {vlan_to_check} is assigned to interface GigabitEthernet0/3")
else:
    print(f"VLAN {vlan_to_check} is not assigned to any interface.")

# The same exercise like above  but with using  a loop

vlan_to_check = input("Provide vlan to be checked:")

# Flag to track if VLAN is found
vlan_found = False

# Loop through each interface and check the VLAN
for interface, config in interface_configs.items():
    if config["vlan"] == vlan_to_check:
        print(f"VLAN {vlan_to_check} is assigned to interface {interface}")
        vlan_found = True

# If the VLAN was not found on any interface
if not vlan_found:
    print(f"VLAN {vlan_to_check} is not assigned to any interface.")

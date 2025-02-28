
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
    counter += 1
print(f"Counter is {counter}")

#The while True: statement creates an infinite loop because True is always evaluated as True,
# meaning the loop condition will never become False. As a result, the loop will continue 
# running indefinitely unless it is manually exited using a break statement, 
# or if some other condition interrupts the flow
#To stop the infinite loop, we typically use a break statement to exit the loop 
# once a specific condition is met

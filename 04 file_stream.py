# Content for "04_ip_addresses.txt"
ip_addresses_content = """192.168.1.1
172.16.0.1
10.0.0.1
192.168.1.2
172.16.0.1  # Duplicate
10.0.0.2
192.168.1.3"""

# Content for "04_routing_table.txt"
routing_table_content = """Destination        Gateway            Flags   Refs      Use   Netif
default            192.168.1.1        UGSc       45        0     en0
10.0.0.0/24        link#2             UCSc        2        0     en1
172.16.0.0/16      172.16.0.1         UGSc        0        0     en2
192.168.1.0/24     link#6             UCSc       10        0     en0"""

# The with statement ensures that the file is properly closed after reading, even if an error occurs.
# This is a cleaner way of working with files because
# you don't have to manually close the file using file.close().


with open("04_ip_addresses.txt" ,"w" ) as file:
    file.write(ip_addresses_content)

with open("04_routing_table.txt", "w") as file:
    file.write(routing_table_content)

"04_ip_addresses.txt" , "04_routing_table.txt"

with open('04_ip_addresses.txt' , 'r') as file:
    contents = file.read()
    print(contents)

# The strip() method is used to remove any leading or trailing whitespace 
# (including newline characters) from each line before printing.

with open( '04_routing_table.txt' , 'r') as file:
    for line in file:
        print(line.strip())

# without strip

with open( '04_routing_table.txt' , 'r') as file:
    for line in file:
        print(line)


#using file.close instead with

file = open('04_routing_table.txt', 'r')  # Open the file in read mode
for line in file:
    print(line.strip())  # Strip and print each line
file.close()  # Manually close the file

subnet_masks = ['255.255.255.0', '255.255.0.0', '255.0.0.0']
with open('04_subnet_masks.txt', 'w') as file:
    for mask in subnet_masks:
        file.write(mask + '\n')


target_network = '192.168.1.0/24'
with open('04_routing_table.txt' , 'r') as file:
    for line in file:
        if target_network in line:
            print(line.strip())

with open( '04_ip_addresses_with_duplicates.txt' , 'r') as file:
    ip_addresses = file.readlines()
# file.readlines() reads all lines of the file and returns them as a list. 
# Each line contains an IP address, possibly with extra spaces or newlines, 
# which will be stripped in the next step.


# A set automatically removes any duplicates, so no extra processing is needed to ensure uniqueness.

unique_ips = set(ip.strip() for ip in ip_addresses)

with open('04_unique_ip_list.txt', 'w') as output_file:
    for ip in unique_ips:
        output_file.write(ip + '\n')

print("Unique IP addresses have been written to '04_unique_ip_list.txt'.")



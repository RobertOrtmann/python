single_quoted_string = 'Hello, Python!'
double_quoted_string = "Hello, Python!"
print(single_quoted_string)
print(double_quoted_string)

greeting = "Hello"
target = "World"
message = greeting + ", " + target + "!"
print(message)

name = "Python"
version = 3.8
message = f"Welcome to {name} version {version} !"
print(message)

a = 5
b = 10
result_message = f"The sum of {a} and {b} is {a + b}."
print(result_message)

length = len(message)
print(length)

cidr_notation = "172.168.1.1/24"
ip_address = cidr_notation.split ('/') [0] # The split('/') method splits the cidr_notation string at the / character into a list of two parts. And [0] dispalys first element of the list
print(ip_address)

first_octet = ip_address[ :ip_address.index('.')]
print(first_octet)

second_octet_start = ip_address.index('.') + 1
second_octet_end = ip_address.index('.', second_octet_start)
second_octet = ip_address[ second_octet_start:second_octet_end ]
print(second_octet)

subnet_mask = cidr_notation.split('/') [1]
print(subnet_mask)

greeting = "Hello, Python!"
sub_greeting = greeting[0:5]
print(sub_greeting)

language = greeting[7:]
print(language)

skip_chars = greeting[::2] # extracts'Hlo yhn'
print(skip_chars)

reversed_greeting = greeting[::-1] # reverse the string
print(reversed_greeting)

last_chars = greeting[-7:]
print(last_chars)

middle_chars = greeting[2:-1] 
print(middle_chars)

nth_chars = greeting[1:10:3]
print(nth_chars)


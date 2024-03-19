my_list = [1, 2, 3, "Python", 3.14]
print(my_list)

first_item=my_list[0] #gets the first item, 1
print(first_item)

my_list.append("new_item")
print(my_list)

my_list.remove("Python")
print(my_list)

for item in my_list:
    print(item)

for index, item in enumerate(my_list):
    print(index, item)

squared_numbers = [x**2 for x in range (10)]
print(squared_numbers)

n = 10
num1 = 0
num2 = 1
next_number = num2  
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

first_row_first_column = matrix[0] [0] #accesses 1
print(first_row_first_column)

for row in matrix:
    print(row)

for row in matrix:
    print(' '.join(map(str, row)))

my_string = "Hello, Python!"
try:
    my_string[7] = 'W' # Trying to replace 'P' with 'W'
except TypeError as e:
    print(e) #strings are imutable in python

my_list = [1, 2, 3, 4]
my_list[2] = 30 # Changing the third element from 3 to 30
print(my_list)

original_list = [1, 2, 3]
new_list = original_list # this copies the reference not the list
new_list[1] = 200 # modifies the original list as well
print(original_list)


independent_copy = original_list[ : ]
independent_copy[1] = 20
print(original_list)
print(independent_copy)

a = 10
b = a
b = 5 # 'a' remains unchanged
print(a)
print(b)


lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1)











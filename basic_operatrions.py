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











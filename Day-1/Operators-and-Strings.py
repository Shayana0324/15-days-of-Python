# Arithmetic Operations in Python

print('Addition = ', 1 + 2)
print('Subtraction = ', 3 - 2)
print('Multiplication = ', 3 * 4)

# Division in python gives floating number
print('Division = ', 4 / 2)
print('Division = ', 9 / 3)
print('Division = ', 9 / 4)

# To get the floating number or without the remainder
print('Division without the remainder = ', 7 // 2)
print('Modulus = ', 5 % 2)                          # Gives the reaminder
print('Exponential = ', 3 ** 2)                     # Calculating 3 * 3

# Floating numbers
print('Floating number,PI = ', 3.14)
print('Floating number, gravity = ', 9.81)

# Complex numbers
print('Complex number = ', 1+1j)
print('Multiplying complex number = ', (1+1j) * (1-1j))

# Declaring the variable at the top first
a = 3           # a: variable name; 3: integer data type
b = 4           # b: variable name; 4: integer data type

# Arithmetic operations & assigning the result to a variable
sum_of_int = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print('a + b = ', sum_of_int)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 5
num_two = 7

# Arithmetic operations
sum_of_int = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Calculating area of a circle
radius = 10
# Two * = exponent or power
area_of_circle = 3.14 * radius ** 2
print('Area of a circle = ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of a rectangle = ', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)                # True: 3 is greater than 2
print(3 >= 2)               # True: 3 is greater than 2
print(3 < 2)                # False: 3 is less than 2
print(2 < 3)                # True: 2 is less than 3
print(2 <= 3)               # True: 2 is less than 3
print(3 == 2)               # False: 3 is not equal to 2
print(3 != 2)               # True: 3 is not equal to 2
print(len('mango') == len('avocado'))       # False
print(len('mango') != len('avocado'))       # True
print(len('mango') < len('avocado'))        # True
print(len('tea') != len('coffee'))          # False
print(len('tea') == len('coffee'))          # True
print(len('tomato') == len('potato'))       # True
print(len('python') > len('dragon'))        # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison
# True - because the data values are the same
print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh')  # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh')  # False -there is no uppercase B
# True - because coding for all has the word coding
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3)  # True - because both statements are true
print(3 > 2 and 4 < 3)  # False - because the second statement is false
print(3 < 2 and 4 < 3)  # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False)  # False
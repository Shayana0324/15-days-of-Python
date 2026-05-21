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


# Strings
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 15 days of python challenge"
print(sentence)

# Multi-line String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 15 days of python.'''
print(multiline_string)
# Another way of doing multi-line string
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 15 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Shayana'
last_name = 'Shrestha'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Shayana Shrestha
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 15

# Unpacking characters
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing
language = 'Python'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?')  # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

# String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'fifteen days of python'
print(challenge.capitalize())  # 'Fifteen days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1
print(challenge.count('th'))  # 1

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
print(challenge.expandtabs())   # 'fifteen  days    of      python'
print(challenge.expandtabs(10))  # 'fifteen    days      of        python'

# find(): Returns the index of first occurrence of substring
print(challenge.find('y'))  # 5
print(challenge.find('ft'))  # 0

# format()	formats string into nicer output
first_name = 'Shayana'
last_name = 'Shrestha'
job = 'GTA'
country = 'USA'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # I am Shayana Shrestha. I am a GTA. I live in USA.

radius = 10
pi = 3.14
area = pi  # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0

# isalnum(): Checks alphanumeric character

challenge = 'FifteenDaysPython'
print(challenge.isalnum())  # True

challenge = '15DaysPython'
print(challenge.isalnum())  # True

challenge = 'fifteen days of python'
print(challenge.isalnum())  # False

challenge = 'fifteen days of python 2026'
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets

challenge = 'fifteen days of python'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'fifteen days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

# isdigit(): Checks Digit Characters

challenge = 'fifteen'
print(challenge.isdigit())  # False
challenge = '15'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '15DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'fifteen_days_of_python'
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'fifteen days of python'
print(challenge.islower())  # True
challenge = 'fifteen days of python'
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters

challenge = 'fifteen days of python'
print(challenge.isupper())  # False
challenge = 'fifteen DAYS OF PYTHON'
print(challenge.isupper())  # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' fifteen days of python '
print(challenge.strip('y'))  # 5

# replace(): Replaces substring inside

challenge = 'fifteen days of python'
print(challenge.replace('python', 'coding'))  # 'fifteen days of coding'

# split():Splits String from Left

challenge = 'fifteen days of python'
print(challenge.split())  # ['fifteen', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'fifteen days of python'
print(challenge.title())  # fifteen Days Of Python

# swapcase(): Checks if String Starts with the Specified String

challenge = 'fifteen days of python'
print(challenge.swapcase())   # fifteen DAYS OF PYTHON
challenge = 'fifteen Days Of Python'
print(challenge.swapcase())  # fifteen dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'fifteen days of python'
print(challenge.startswith('fifteen'))  # True
challenge = '15 days of python'
print(challenge.startswith('fifteen'))  # False




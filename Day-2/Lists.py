empty_list = list()                 # this is an empty list - no item in the list

# list of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']             # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yogurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']    # list of web technologies
countries = ['Australia', 'Nepal', 'Germany', 'USA', 'Switzerland']

# Print the lists and its length
print('Fruits: ', fruits)
print('Number of fruits: ', len(fruits))
print('Vegetables: ', vegetables)
print('Number of vegetables: ', len(vegetables))
print('Animal products: ', animal_products)
print('Number of animal products: ', len(animal_products))
print('Web technologies: ', web_techs)
print('Number of web technologies: ', len(web_techs))
print('Number of countries: ', len(countries))

# Modifying list
fruits = ['banana', 'orange', 'mango', 'lemon']

first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruit = fruits[3]
print(last_fruit)
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]

# Accessing items
last_fruit = fruits[-1]
secong_last = fruits[-2]
print(last_fruit)           # lemon
print(second_last)          # mango

# Slicing items
all_fruits = fruits[0:4]        # returns all fruits
all_fruits = fruits[0:]         # gives the same result as above. if we don't set where to stop, it takes all the rest
orange_and_mango = fruits[1:3]  # it does not include the end index
orange_and_lemon = fruits[-3:]

fruits[0] = 'Avocado'
print(fruits)       # ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       # ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits)
fruits[last_index] = 'lime'
print(fruits)       # ['avocado', 'apple', 'mango', 'lime']



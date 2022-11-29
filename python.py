'''
PYTHON
A high-level interpreted programming language

Like JavaScript, Python is a dynamic scripting language that doesn't have to be compiled before it can be executed - it runs within an interpreter that handles the conversion into machine code

Python is an Object-Oriented Programming (OOP) Language: programming with objects representing the real-world objects of an app

In other words, everything in Python is an object

Common for server side applications, big data analysis, and machine learning, and can make web apps with Django and Flask

Can make ".py" or ".ipynb" files

Table of Contents:
THE VERY BASICS
VARIABLES, DATA AND VALUES
DOING MATH
PLAYING WITH STRINGS (WORDS)
EXPRESSIONS AND LOOPS
DICTIONARIES
LISTS
TUPLES
OBJECTS, CLASSES, AND OOP
FUNCTIONS
'''

################## THE VERY BASICS ##########################
# this is a comment

'''
this is a comment,
with multiple lines,
sometimes known as "docstrings"
'''

# to call the script in the terminal
# > python3 python.py (or whatever <filename> you have)

# print(), essentially's Python's console.log()
print('Hello, World')  # Hello, World

############ VARIABLES, DATA AND VALUES #####################
# overall Python syntax for variables
# case sensitive, follows snake_case
py_variable = 'value'

# data types
str = 'hello'
bool = True
int = 15
float = 3.14
complex = 3+4j  # "j" filling in for the square root of a negative number
none_type = None  # like JS "null", nothingness

'''
"falsey" values in Python:
False
None
0, 0.0, 0j
'', [], (), {}, range(0)
'''

################### DOING MATH ##############################
# math operations
add = 3 + 2
subtract = 3 - 2
multiply = 3 * 2
divide = 3 / 2  # 1.5
quotient = 3 // 2  # 1, always rounding down
modulo_remainder = 3 % 2  # returns the remainder of dividing two numbers
exponentiation = 3 ** 2  # like 3^2

############# PLAYING WITH STRINGS (WORDS) ##################
# combining (concatenating) strings
little_str = 'bad'
big_str = 'super'
concat_str = big_str + little_str  # superbad

# string interpolation
state = 'Hawaii'
year = 1959
f_string = f'{state} joined the US in {year}'  # Hawaii joined the US in 1959

# string methods
str_split = 'ace of spades'.split(" ")  # ['ace', 'of', 'spades']
str_list = list('abc')  # ['a', 'b', 'c']
str_index = 'qqxzzz'.index('x')  # 2
str_upper = 'Boo'.upper()  # BOO
str_lower = 'Boo'.lower()  # boo
str_replace = 'I love me'.replace('me', 'you')  # I love you
str_in = 'eggs' in 'green eggs and ham'  # True

# built-in functions (for strings and more)
str_len = len('tacos')  # 5
str_brackets = 'course'
print(str_brackets[1])  # o
print(str_brackets[-1])  # e

'''
Operators:
< - less than
> - greater than
<= - less than or equal
>= - greater than or equal
== - equal to
!= - not equal to (can also use <>)
or - or
and - and
'''

############# EXPRESSIONS AND LOOPS #########################
# if, elif, else expressions (only use what you need)
floor = 'sticky'
if floor == 'sticky':
    print('floor is sticky')
elif floor == 'clean':
    print('floor is clean')
else:
    print('who knows!')

# ternary expression
age = 30
beverage = 'Beer' if age >= 21 else 'Milk'

# for looping
names = ['Tom', 'Tim', 'Simon']
for name in names:
    print(name)
    # Tom
    # Tim
    # Simon

# while looping (great when you don't know how many times you need to iterate)
n, i = 4, 1
while i <= n:
    print(i)
    i += 1
    # 1
    # 2
    # 3
    # 4

# range
for num in range(5):
    print(num)
    # 0
    # 1
    # 2
    # 3
    # 4

# range (w/ a start and step)
# start at 2, stop by 10, go by every 2 steps
for even in range(2, 10, 2):
    print(even)
    # 2
    # 4
    # 6
    # 8

# negative range (counting down)
for num in range(5, 0, -1):
    print(num)
    # 5
    # 4
    # 3
    # 2
    # 1

# range turning into lists
nums = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# range turning into tuples
odds = tuple(range(1, 10, 2))  # (1, 3, 5, 7, 9)

################# DICTIONARIES ##############################
# Python's objects w/ key-value pairs)
student = {
    'name': 'Brady',
    'favorite_color': 'Blue',
    'age': 30
}  # {'name': 'Brady', 'favorite_color': 'Blue', 'age': 30}
student_name = student['name']  # Brady
student.keys() # dict_keys(['name', 'favorite_color', 'age'])
student.values() # dict_values(['Brady', 'Blue', 30])

# changing values in a dict
student['name'] = 'Bradly'  # sets the "name" value to now be "Bradly"

# the dict "in" operator
if 'favorite_color' in student:
    print(f"{student['name']}'s favorite color is {student['favorite_color']}")
else:
    print(f"{student['name']} doesn't have a favorite color")

# adding items to a dict
# {'name': 'Bradly', 'favorite_color': 'Blue', 'age': 30, 'location': 'North Campus'}
student['location'] = 'North Campus'

# deleting items from a dict
del student['location']  # "'location' in student" should equal False

# retrieve number of items in a dict
len(student)  # 3

# iterating over items in a dict
# dict_items([('name', 'Bradly'), ('favorite_color', 'Blue'), ('age', 30)])
student.items()
for key, val in student.items():
    print(f"{key} = {val}")
    # name = Bradly
    # favorite_color = Blue
    # age = 30

####################### LISTS ##############################
# Python's arrays
colors = ['red', 'green', 'blue']

# retrieve number of items in a list
len(colors)  # 3
colors.count('red')  # 1

# accessing items in a list
colors[1]  # green
colors[-1]  # blue
print(*colors)  # red green blue

# slicing a list: where to start, where to start "slicing"
colors[0:2]  # ['red', 'green']
colors[:-1]  # ['red', 'green']

# assigning and updating items in a list
colors[-1] = 'black'  # ['red', 'green', 'black']

# adding one item to a list
colors.append('pink')  # ['red', 'green', 'black', 'pink']

# adding multiple items to a list
# ['red', 'green', 'black', 'pink', 'orange', 'purple']
colors.extend(['orange', 'purple'])

# inserting an item anywhere in a list
# ['red', 'yellow', 'green', 'black', 'pink', 'orange', 'purple']
colors.insert(1, 'yellow')

# removing a specific item in a list
# pop() by itself removes just the last item
colors.pop(2)  # ['red', 'yellow', 'black', 'pink', 'orange', 'purple']

# removing the first instance of a specific item in a list
colors.remove('orange')  # ['red', 'yellow', 'black', 'pink', 'purple']

# deleting a section in a list
# starting item to cut, starting item to keep
del colors[1:3]  # ['red', 'pink', 'purple']

# clear an entire list
colors.clear()  # []

# combining lists into one list
odds = [1, 3, 5]
evens = [2, 4, 6]
nums = odds + evens  # [1, 3, 5, 2, 4, 6]

# adding up a list
sum(nums)  # 21

# joining a list as a string
str = 'TACOS'
str_join = ",".join(str)  # T,A,C,O,S

# reversing a list (in place)
nums.reverse()
print(nums)  # [6, 4, 2, 5, 3, 1]

# sort() itself returns None, which means there is no return value since it just modifies the original list; it does NOT return a new list by itself
nums.sort()
print(nums)  # [1, 2, 3, 4, 5, 6]

sorted_copy = sorted(nums)  # [1, 2, 3, 4, 5, 6]

# iterating over items in a list
for num in nums:
    print(num)
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6

# iterating over items in a list w/ each index (enumerate)
for idx, num in enumerate(nums):
    print(idx, num)
    # 0 1
    # 1 2
    # 2 3
    # 3 4
    # 4 5
    # 5 6

# list comprehensions (Python's version of mapping)
# I want <expression> for each <item> in <list>
squares = [n * n for n in nums]  # [1, 9, 25, 4, 16, 36]

# filtering items while mapping a list
# I want <expression> for each <item> in <list> if <conditional>
even_squares = [n * n for n in nums if (n * n) % 2 == 0]  # [4, 16, 36]

# combining lists into tuples (more on tuples in a sec)
dinner = ['taco', 'burger', 'pizza']
breakfast = ['eggs', 'toast', 'coffee']
food_zip = zip(breakfast, dinner)
# {('coffee', 'pizza'), ('eggs', 'taco'), ('toast', 'burger')}
print(set(food_zip))

####################### TUPLES ##############################
# Like lists, but immutable once made
# list: good for similar data types
# tuples: good for different data types
states = ('indiana', 'new york', 'illinois')
len(states)  # 3

# if trying to create a 1-tuple
hello_tuple = ('Hello',)

# accessing items in a tuple
states[1]  # new york

# accessing the index of the first match inside a tuple
states.index('illinois')  # 2

# iterating over a tuple
for idx, state in enumerate(states):
    print(idx, state)
    # 0 indiana
    # 1 new york
    # 2 illinois

# unpacking a tuple (performing multiple variable assignments in one line)
IN, NY, IL = states
print(IN, NY, IL)  # indiana new york illinois

# slicing tuples (starting value to keep, starting value to slice away)
short_name = 'Alexandria'[0:4]  # Alex
shorter_name = 'Alexandria'[:2]  # Al
slice_until_the_end = 'Alexandria'[1:]  # lexandria

############ OBJECTS, CLASSES, AND OOP ######################
# listing an object's members (attributes and methods)
# __methods__ are called "magic" (dunder) methods
pizza_toppings = ['cheese', 'pepperoni', 'fish']
dir(pizza_toppings)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# creating an object w/ attributes and one default parameter
# __init__ is short for "initialize", used to initialize the properties of the new object
# "self" is Python's version of JS "this"
# "bark" is an "instance" method in this Dog class
# __str__ allows us to override our method to print our objects


class Dog():
    next_id = 1  # class attribute

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        self.id = Dog.next_id
        Dog.next_id += 1

    def bark(self):
        print(f"{self.name} says woof!")

    def __str__(self):
        return f"Dog ({self.id}) named {self.name} is {self.age} years old"

    @classmethod
    def get_total_dogs(cls):  # cls represents the Dog class
        return cls.next_id - 1


spot = Dog('Spot', 8)
print(spot.name, spot.age)  # Spot 8
spot.bark()  # Spot says woof!
print(spot)  # Dog (1) named Spot is 8 years old

lassie = Dog('Lassie')
print(lassie.name, lassie.age)  # Lassie 0
lassie.bark()  # Lassie says woof!
print(lassie)  # Dog (2) named Lassie is 0 years old

Dog.get_total_dogs()  # 2

# creating a subclass (CamelCase)


class ShowDog(Dog):
    def __init__(self, name, age=0, total_earnings=0):
        Dog.__init__(self, name, age)  # init the old from superclass
        self.total_earnings = total_earnings  # then add in the new

    def add_prize_money(self, amount):  # adding more methods
        self.total_earnings += amount


winky = ShowDog('Winky', 3, 1000)
print(winky)  # Dog (3) named Winky is 3 years old
winky.bark()  # Winky says woof!
print(winky.total_earnings)  # 1000
winky.add_prize_money(500)
print(winky.total_earnings)  # 1500

#################### FUNCTIONS ##############################


def spam():
    eggs = 10
    return eggs


spam()  # 10


def add(a, b):
    return a + b


add(1, 2)  # 3

# anonymous (lambda) functions
# lambda <args> : <exp>
# like JS arrow functions, good for mapping
numbers = [1, 2, 3, 4, 5, 6]
doubled_numbers = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25, 36]

################ PY SOLUTIONS TO KNOW WELL ##################
# todo Palindrome

# todo FizzBuzz

# todo Fibonacci

################# Thank you for reading :) ##################

'''
Helpful Python links
Official Python website https://www.python.org/
Python in 100 Seconds https://www.youtube.com/watch?v=x7X9w_GIm1s
Python tutorials https://realpython.com/
Another Python cheatsheet https://devhints.io/python

Thank you, General Assembly!
'''

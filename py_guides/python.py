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
hello_tuple = ('Hello', )

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

################ PY SOLUTIONS TO KNOW ##################
# todo Palindrome

# todo FizzBuzz

# todo Fibonacci
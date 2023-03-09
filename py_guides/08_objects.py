"""

Objects can include and list attributes and methods
"""
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

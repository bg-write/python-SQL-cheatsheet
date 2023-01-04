"""

How to write a typical function
"""


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

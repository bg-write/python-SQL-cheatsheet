"""

overall Python syntax for variables
case sensitive, follows snake_case
"""
py_variable = 'value'

# data types
string = 'hello'
boolean = True
int = 15
float = 3.14
complex = 3 + 4j  # "j" filling in for the square root of a negative number
none_type = None  # like JS "null", nothingness
list = [1, 2, 3]
dictionary = {'name': 'Bob', 'job': 'writer'}
set = {9.8, 3.14, 2.7} # can only store unique items
tuple = (9.8, 3.14, 2.7) # cannot be modified once they're created; immutable
'''
"falsey" values in Python:
False
None
0, 0.0, 0j
'', [], (), {}, range(0)
'''

# to check data types
print(type(10))  # int

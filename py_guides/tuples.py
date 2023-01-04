"""

Tuples are like lists, but they're immutable once made
list: good for similar data types
tuples: good for different data types
"""
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

"""

if, elif, else, ternary, for, while, range
"""
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

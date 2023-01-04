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
string = 'TACOS'
string_join = ','.join(str)  # T,A,C,O,S

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

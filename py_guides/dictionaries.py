"""

Python's objects w/ key-value pairs)
"""
student = {
    'name': 'Brady',
    'favorite_color': 'Blue',
    'age': 30
}  # {'name': 'Brady', 'favorite_color': 'Blue', 'age': 30}
student_name = student['name']  # Brady
student.keys()  # dict_keys(['name', 'favorite_color', 'age'])
student.values()  # dict_values(['Brady', 'Blue', 30])

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

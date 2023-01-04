"""

Playing with words
"""
# combining (concatenating) strings
little_str = 'bad'
big_str = 'super'
concat_str = big_str + little_str  # superbad

# string interpolation
state = 'Hawaii'
year = 1959
f_string = f'{state} joined the US in {year}'  # Hawaii joined the US in 1959

# string methods
str_split = 'ace of spades'.split(' ')  # ['ace', 'of', 'spades']
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

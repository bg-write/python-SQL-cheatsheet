"""TABLE OF CONTENTS
-Palindrome
-FizzBuzz
-Fibonacci
-Reverse String
"""

# ---------------------------------------------------
# Palindrome
# Check if a string is spelled the same both forward and backward, ignoring case and non-alphanumeric characters (punctuation, spaces, symbols)

import re

str_to_check = 'raceC@_ar'


def palindrome(str):
    str_alphabet = re.sub(r'[\W_]', '', str)
    str_clean = str_alphabet.lower().replace(' ', '')
    return str_clean == str_clean[::-1]


palindrome(str_to_check)  # True

# ---------------------------------------------------
# FizzBuzz
# Write a program that prints any range of numbers. For multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."

for num in range(1, 16):
    str = ''
    if num % 3 == 0:
        str = str + 'Fizz'
    if num % 5 == 0:
        str = str + 'Buzz'
    else:
        str = num
    print(str)
# 1
# 2
# 3
# 4
# Buzz
# 6
# 7
# 8
# 9
# Buzz
# 11
# 12
# 13
# 14
# FizzBuzz

# ---------------------------------------------------
# Fibonacci
# Using recursion, find the nth element within the Fibonacci Sequence


def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(0)  # 0
fibonacci(1)  # 1
fibonacci(2)  # 1
fibonacci(3)  # 2
fibonacci(4)  # 3
fibonacci(5)  # 5
fibonacci(6)  # 8

# ---------------------------------------------------
# Reverse String
# Write a function that reverses a string.
# The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

s1 = ['h', 'e', 'l', 'l', 'o']
s2 = ['H', 'a', 'n', 'n', 'a', 'h']


def reverse_string(s):
    return s[::-1]


reverse_string(s1)  # ['o', 'l', 'l', 'e', 'h']
reverse_string(s2)  # ['h', 'a', 'n', 'n', 'a', 'H']

# ---------------------------------------------------
# TBD
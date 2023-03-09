# Palindrome
# Check if a string is spelled the same both forward and backward, ignoring case and non-alphanumeric characters (punctuation, spaces, symbols)
import re

str_to_check = 'raceC@_ar'


def palindrome(str):
    str_alphabet = re.sub(r'[\W_]', '', str)
    # [^...] / if we catch a character NOT in the ranges stated after ^, then replace it with ''
    # https://regex101.com/
    str_clean = str_alphabet.lower().replace(' ', '')
    return str_clean == str_clean[::-1]
    # [::-1] is slice notation for "start at the end, count down to the beginning, and take one step back at a time"


palindrome(str_to_check)  # True

# FizzBuzz
# Write a program that prints any range of numbers. For multiples of three, print "Fizz" instead of the number. For multiples of five, print "Buzz." For numbers that are multiples of both three and five, print "FizzBuzz."
for num in range(1, 31):
    str = ''
    if num % 3 == 0:
        str = str + 'Fizz'
    if num % 5 == 0:
        str = str + 'Buzz'
    else:
        str = num
    print(str)


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

# Euclidian Distance
# Find an Euclidian distance between (2, 3) and (10, 8) aka find the shortest distance between two or more points in two or more dimensions
from math import dist

point_1 = (2, 3)
point_2 = (10, 8)
euclidian_distance = dist(point_1, point_2)
# 9.433981132056603
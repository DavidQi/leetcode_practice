#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]"""


def fizz_buzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    return ['Fizz'*(not i % 3) + 'Buzz'*(not i % 5) or str(i) for i in range(1, n+1)]

if __name__ == '__main__':
    print(fizz_buzz(15))

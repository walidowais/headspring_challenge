#!/usr/bin/env python
# Name: Walid Owais
# Filename: fizzbuzz.py
# Headspring skills assessment

import unittest

"""
Input: integers start and end for range to render FizzBuzz
Output: string result that contains FizzBuzz result over range
"""
def render(start = 0, end = 100):
	if type(start) != int or type(end) != int:
		raise ValueError("invalid type for start or end, must be int")

	result = ""
	i = start
	while i <= end:
	  if (i % 3 == 0) and (i % 5 == 0):
	    result += "FizzBuzz"
	  elif i % 3 == 0:
	    result += "Fizz"
	  elif i % 5 == 0:
	    result += "Buzz"
	  else:
	    result += str(i)
	  i += 1
	  result += "\n"
	return result

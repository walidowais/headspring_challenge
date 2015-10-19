#!/usr/bin/env python
# Name: Walid Owais
# Filename: fizzbuzz.py
# Headspring skills assessment

def render():
	result = ""
	i = 1
	while i <= 100:
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

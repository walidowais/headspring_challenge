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

class FizzBuzzTest(unittest.TestCase):
  """Unit testing for fizzbuzz module"""
  
  def test_fizz(self):
    result = render(3,3)
    self.assertTrue("Fizz" in result)
    self.assertFalse("Buzz" in result)

  def test_buzz(self):
    result = render(5,5)
    self.assertTrue("Buzz" in result)
    self.assertFalse("Fizz" in result)

  def test_fizzbuzz(self):
    result = render(15,15)
    self.assertTrue("FizzBuzz" in result)

  def test_invalid_range(self):
    result = render(100, 10)
    self.assertFalse("Fizz" in result)
    self.assertFalse("Buzz" in result)
    self.assertFalse("17" in result)

  def test_invalid_type(self):
    try:
      result = render("0", "100")
    except ValueError:
      pass
    else:
      self.fail("Did not see ValueError")

if __name__ == '__main__':
  unittest.main()

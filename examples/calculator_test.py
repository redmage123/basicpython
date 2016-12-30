#!/usr/bin/env python
import unittest

# This is the class that we're going to test
from calculator import Calculator
 
""" Run this program by calling 'nosetests calculator_test.py' 
     You must install nosetests manually via the pip command.
     If you don't have pip installed, then, again you need
     to install that as well. 
"""
# The test case class imports from unittest.TestCase
class TddInPythonExample(unittest.TestCase):
    

# Setup the object. 
    def setUp(self):
        self.calc = Calculator()

# All test cases need to start with the string 'test_' so that nosetests
# can find and execute it. 


    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2,2)
        self.assertEqual(4, result)

    def test_calculator_sub_method_returns_correct_results(self):
        result = self.calc.sub(2,2)
        self.assertEqual(0, result)

    def test_calculator_mul_method_returns_correct_results(self):
        result = self.calc.mul(2,2)
        self.assertEqual(4,result)

    def test_calculator_div_method_returns_correct_results(self):
        result=self.calc.div(2,2)
        self.assertEqual(1,result)


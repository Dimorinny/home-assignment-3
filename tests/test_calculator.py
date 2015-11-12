# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from calc import Operator, evaluate
from custom_operator import add, sub, mul, truediv, sin
from math import pi
import unittest

class EvaluateTestCase(unittest.TestCase):
	def test_not_supported_method(self):
		with self.assertRaises(ValueError):
			evaluate("not_supported", 1, 2)

	def test_supported_method(self):		
		self.assertAlmostEqual(evaluate("+", 1, 2), 3)

class OperatorTestCase(unittest.TestCase):
	def setUp(self):
		self.sin = Operator(sin, 1)
		self.truediv = Operator(truediv, 2)

	def test_invalid_count_args(self):
		with self.assertRaises(ValueError):
			self.sin(1, 2)

	def test_div_null(self):
		with self.assertRaises(ZeroDivisionError):
			self.truediv(2, 0)

class OperatorsTestCase(unittest.TestCase):
	def setUp(self):
		self.sin = sin
		self.add = add
		self.sub = sub
		self.mul = mul
		self.truediv = truediv

	def test_add(self):
		self.assertAlmostEqual(self.add(2, 3.5), 5.5)

	def test_sub(self):
		self.assertAlmostEqual(self.sub(2, 3.5), -1.5)

	def test_mul(self):
		self.assertAlmostEqual(self.mul(2, 3.5), 7)

	def test_truediv(self):
		self.assertAlmostEqual(self.truediv(2, 4), 0.5)

	def test_sin(self):
		self.assertAlmostEqual(self.sin(1), 0.8414709848)

	def test_sub2(self):
		self.assertEqual(self.sub(0.3, 0.1), 0.2)

	def test_sin2(self):
		self.assertEqual(self.sin(pi/6), 0.5)

		

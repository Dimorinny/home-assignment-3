# -*- coding: utf-8 -*-

import sys
sys.path.append('../')

from calc import Operator, evaluate
from operator import add, sub, mul, truediv
from math import sin
import unittest

class EvaluateTestCase(unittest.TestCase):
	def test_not_supported_method(self):
		with self.assertRaises(TypeError):
			evaluate("not_supported", 1, 2)

	def test_supported_method(self):		
		self.assertEqual(evaluate("+", 1, 2), 1 + 2)

class OperatorsTestCase(unittest.TestCase):
	def setUp(self):
		self.add = Operator(add, 2)
		self.sub = Operator(sub, 2)
		self.mul = Operator(mul, 2)
		self.sin = Operator(sin, 1)
		self.truediv = Operator(truediv, 2)

	def test_add(self):
		self.assertEqual(self.add(2, 3.5), 2 + 3.5)

	def test_sub(self):
		self.assertEqual(self.sub(2, 3.5), 2 - 3.5)

	def test_mul(self):
		self.assertEqual(self.mul(2, 3.5), 2 * 3.5)

	def test_truediv(self):
		self.assertEqual(self.truediv(2, 3.5), 2 / 3.5)

	def test_sin(self):
		self.assertEqual(self.sin(2), sin(2))

	def test_invalid_count_args(self):
		with self.assertRaises(TypeError):
			self.sin(1, 2)

	def test_div_null(self):
		with self.assertRaises(ZeroDivisionError):
			self.truediv(2, 0)
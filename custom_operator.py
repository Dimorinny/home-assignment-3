# -*- coding: utf-8 -*-

# normal div from python3
from __future__ import division
from math import sin as _sin

def round_decarator(func):
	def _decorator(*args, **kwargs):
		return round(func(*args, **kwargs), 10)

	return _decorator

@round_decarator
def add(op1, op2):
	return op1 + op2

@round_decarator
def sub(op1, op2):
	return op1 - op2

@round_decarator
def mul(op1, op2):
	return op1 * op2

@round_decarator
def truediv(op1, op2):
	return op1 / op2

@round_decarator
def sin(op1):
	return _sin(op1)
# -*- coding: utf-8 -*-

from operator import add, sub, mul, truediv
from math import sin
import unittest
import argparse
 
class Operator(object):
        def __init__(self, operator, args_count):
                self.operator = operator
                self.args_count = args_count
 
        def __call__(self, *args):
                if len(args) != self.args_count:
                        raise TypeError("Invalid args count. Right is " + str(self.args_count))
 
                return self.operator(*args)
 
operators = {
        "+": Operator(add, 2),
        "-": Operator(sub, 2),
        "*": Operator(mul, 2),
        "/": Operator(truediv, 2),
        "sin": Operator(sin, 1)
}
 
def evaluate(operator, *args):
        if operator not in operators:
                raise TypeError("Our calculator does not support operator: " + operator)
        return operators[operator](*args)
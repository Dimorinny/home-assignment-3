# -*- coding: utf-8 -*-

from calc import evaluate
import argparse

def main():
	parser = argparse.ArgumentParser(description='Process operator and arguments')	
	parser.add_argument('operator')
	parser.add_argument('arguments', type=float, nargs='+')

	args = parser.parse_args()

	try:
		print evaluate(args.operator, *args.arguments)
	except Exception as e:
		print "Error: " + e.message

if __name__ == "__main__":
	main()
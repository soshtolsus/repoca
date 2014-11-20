#!/usr/bin/env python3

#Copyright 2014 Carl Johnson IV

'''
command line rpn calculator
'''

#TODO: allow for function definition inline (ephemeral) and in config (persistent)

import argparse
import sys
from decimal import Decimal

from command import Command
from stack import Stack


COMMAND_DEFINITIONS = {
	'p': Command(0, 0, lambda x: print(x.peek())),
	'f': Command(0, 0, lambda x: print('\n'.join([str(a) for a in x.walk()]))),
	'+': Command(2, 1, lambda _,x,y: x+y),
	'-': Command(2, 1, lambda _,x,y: y-x),
	'*': Command(2, 1, lambda _,x,y: x*y),
	'/': Command(2, 1, lambda _,x,y: y/x)
}


def getargs():
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument('commands', nargs='+', help='commands and data to process')

	return parser.parse_args()

def main(args):
	stack = Stack()

	for command_key in args.commands:
		if command_key in COMMAND_DEFINITIONS:
			COMMAND_DEFINITIONS[command_key](stack)
		else:
			stack.push(Decimal(command_key)) #it's a value

	if stack.peek() is not None:
		COMMAND_DEFINITIONS['f'](stack)

if __name__=='__main__':
	try:
		main(getargs())
	except KeyboardInterrupt:
		print('exiting gracefully', file=sys.stderr)

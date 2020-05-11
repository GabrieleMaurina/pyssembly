#!/usr/bin/env python

from sys import argv
from shlex import split
from random import uniform, randint
import math



######################################################################################
#CONVERSIONS#
######################################################################################



def is_int(v):
	try:
		int(v)
	except (TypeError, ValueError):
		return False
	else:
		return True

def is_float(v):
	try:
		float(v)
	except (TypeError, ValueError):
		return False
	else:
		return True

def is_string(v):
	if v and ((v.startswith('\'') and v.endswith('\'')) or (v.startswith('\"') and v.endswith('\"'))):
		return True
	else:
		return False

def string(v):
	return v[1:-1].replace('\\n', '\n')

def is_null(v):
	return v == 'null'

def null(v):
	return None

def is_bool(v):
	return v == "True" or v == "False"

def cast_bool(v):
	return v != 'False'	

def is_id(v):
	return v and not is_int(v) and not is_float(v) and not is_string(v) and not is_null(v) and not is_bool(v)



######################################################################################
#UTILS#
######################################################################################



def get(v, variables):
	if is_int(v): return int(v)
	elif is_float(v): return float(v)
	elif is_string(v): return string(v)
	elif is_null(v): return null(v)
	elif is_bool(v): return cast_bool(v)
	elif v in variables: return variables[v]
	else: raise SyntaxError('Undefined token: ' + v)

def get_variable(v, variables):
	if v in variables: return variables[v]
	else: raise SyntaxError('Undefined variable: ' + v)

def assign1(a, b, f, variables):
	if not is_id(a): raise SyntaxError('Wrong identifier: ' + a)
	b = get(b, variables)
	variables[a] = f(b)

def assign2(a, b, f, variables):
	a_value = get_variable(a, variables)
	b = get(b, variables)
	variables[a] = f(a_value, b)



######################################################################################
#GENERAL#
######################################################################################



def my_in(a, b, variables):
	assign1(a, b, lambda b: input(b), variables)

def out(a, b, variables):
	a = get(a, variables)
	b = get(b, variables)
	if a is not None: print(a, end='')
	if b is not None: print(b, end='')

def mov(a, b, variables):
	assign1(a, b, lambda b: b, variables)

def jmp(a, b, variables):
	a = get(a, variables)
	if not is_id(b): raise SyntaxError('Wrong label: ' + b)
	if a: return b



######################################################################################
#CONVERSIONS#
######################################################################################



def my_bool(a, b, variables):
	assign1(a, b, lambda b: bool(b), variables)

def my_int(a, b, variables):
	assign1(a, b, lambda b: int(b), variables)

def my_float(a, b, variables):
	assign1(a, b, lambda b: float(b), variables)

def my_string(a, b, variables):
	assign1(a, b, lambda b: string(b), variables)



######################################################################################
#MATH#
######################################################################################



def add(a, b, variables):
	assign2(a, b, lambda a, b: a+b, variables)

def sub(a, b, variables):
	assign2(a, b, lambda a, b: a-b, variables)

def mul(a, b, variables):
	assign2(a, b, lambda a, b: a*b, variables)

def div(a, b, variables):
	assign2(a, b, lambda a, b: a/b, variables)

def pow(a, b, variables):
	assign2(a, b, lambda a, b: a**b, variables)

def log(a, b, variables):
	assign2(a, b, lambda a, b: math.log(a, b), variables)

def root(a, b, variables):
	assign2(a, b, lambda a, b: a**(1/b), variables)

def idiv(a, b, variables):
	assign2(a, b, lambda a, b: a//b, variables)

def mod(a, b, variables):
	assign2(a, b, lambda a, b: a%b, variables)



######################################################################################
#RANDOM#
######################################################################################



def rnd(a, b, variables):
	assign2(a, b, lambda a, b: uniform(a, b), variables)

def irnd(a, b, variables):
	assign2(a, b, lambda a, b: randint(a, b), variables)



######################################################################################
#TRIGONOMETRY#
######################################################################################



def sin(a, b, variables):
	assign1(a, b, lambda a, b: math.sin(b), variables)

def cos(a, b, variables):
	assign1(a, b, lambda a, b: math.cos(b), variables)

def tan(a, b, variables):
	assign1(a, b, lambda a, b: math.tan(b), variables)

def asin(a, b, variables):
	assign1(a, b, lambda a, b: math.asin(b), variables)

def acos(a, b, variables):
	assign1(a, b, lambda a, b: math.acos(b), variables)

def atan(a, b, variables):
	assign1(a, b, lambda a, b: math.atan(b), variables)

def atan2(a, b, variables):
	assign2(a, b, lambda a, b: math.atan2(a, b), variables)



######################################################################################
#BOOLEAN#
######################################################################################



def eq(a, b, variables):
	assign2(a, b, lambda a, b: a == b, variables)

def neq(a, b, variables):
	assign2(a, b, lambda a, b: a != b, variables)

def les(a, b, variables):
	assign2(a, b, lambda a, b: a < b, variables)

def leq(a, b, variables):
	assign2(a, b, lambda a, b: a <= b, variables)

def grt(a, b, variables):
	assign2(a, b, lambda a, b: a > b, variables)

def geq(a, b, variables):
	assign2(a, b, lambda a, b: a >= b, variables)

def my_not(a, b, variables):
	assign1(a, b, lambda b: not b, variables)

def my_and(a, b, variables):
	assign2(a, b, lambda a, b: a and b, variables)

def my_or(a, b, variables):
	assign2(a, b, lambda a, b: a or b, variables)

def xor(a, b, variables):
	assign2(a, b, lambda a, b: a != b, variables)

def nand(a, b, variables):
	assign2(a, b, lambda a, b: not(a and b), variables)

def nor(a, b, variables):
	assign2(a, b, lambda a, b: not(a or b), variables)

def nxor(a, b, variables):
	assign2(a, b, lambda a, b: a == b, variables)



######################################################################################
#INSTRUCTION SET#
######################################################################################



functions = {
#General
	'in': my_in,
	'out': out,
	'mov': mov,
	'jmp': jmp,
#Conversions
	'bool': my_bool,
	'int': my_int,
	'flt': my_float,
	'str': my_string,
#Math
	'add': add,
	'sub': sub,
	'mul': mul,
	'div': div,
	'pow': pow,
	'log': log,
	'root': root,
	'idiv': idiv,
	'mod': mod,
#Random
	'rnd': rnd,
	'irnd': irnd,
#Trigonometry
	'sin': sin,
	'cos': cos,
	'tan': tan,
	'asin': asin,
	'acos': acos,
	'atan': atan,
	'atan2': atan2,
#Boolean
	'eq': eq,
	'neq': neq,
	'les': les,
	'leq': leq,
	'grt': grt,
	'geq': geq,
	'not': my_not,
	'and': my_and,
	'or': my_or,
	'xor': xor,
	'nand': nand,
	'nor': nor,
	'nxor': nxor
}



######################################################################################
#COMPILE#
######################################################################################



def compile_instruction(position, instruction, labels):
	tokens =  split(instruction, posix=False)
	if len(tokens) == 0 or tokens[0].startswith(';'):
		return ()
	elif len(tokens) == 1:
		if not is_id(tokens[0]): raise SyntaxError('Invalid label: ' + tokens[0])
		if tokens[0] in labels: raise SyntaxError('Label already used: ' + tokens[0])
		labels[tokens[0]] = position + 1
		return (tokens[0],)
	elif len (tokens) == 3:
		if tokens[0] not in functions: raise SyntaxError('Unknown instruction: ' + tokens[0])
		return (functions[tokens[0]], tokens[1], tokens[2])
	else:
		raise SyntaxError('Wrong instruction: ' + str(tokens))

def compile_program(prog):
	labels = {}
	instructions = [compile_instruction(position, instruction, labels) for position, instruction in enumerate(prog.split('\n'))]
	if not instructions[-1]: del instructions[-1]
	return (instructions, labels)

def compile_file(path):
	with open(path, 'r') as source:
		return compile_program(source.read())



######################################################################################
#EXECUTE#
######################################################################################



def execute_instruction(instruction, labels, program_counter, variables):
	res = None
	if len(instruction) == 3:
		res = instruction[0](instruction[1], instruction[2], variables)
	if is_int(res):
		return int(res)
	elif is_id(res):
		if res not in labels: raise ValueError('Unknown label: ' + res)
		return labels[res]
	else:
		return program_counter + 1

def execute_program(instructions, labels, variables):
	program_counter = 0
	tot = len(instructions)
	while program_counter < tot:
		program_counter = execute_instruction(instructions[program_counter], labels, program_counter, variables)

def execute_file(path, variables):	
	compiled = compile_file(path)
	#print(compiled)
	execute_program(*compiled, variables)



######################################################################################
#MAIN#
######################################################################################



def main():
	if len(argv) > 1:
		execute_file(argv[1], {})
	else:
		print('Usage: python -m pyssembly <code.pys>\n\nPyssembly allows to execute pseudo assembly code and it is meant for teaching purposes.\n\nFind out more at https://github.com/GabrieleMaurina/pyssembly')

if __name__ == '__main__':
	main()

# Day 5: Supply Stacks
import numpy as np

# a function that returns the first n rows of a file
def head(filename, n=10):
    with open(filename) as f:
        return f.readlines()[:n]

# a function that returns all rows after he nth row of a file
def tail(filename, n=10):
    with open(filename) as f:
        return f.readlines()[n:]

# given a list of strings, remove any newline characters and pad all of the strings on the right to be the same length
def pad_right(stack):
    stack = [s.rstrip() for s in stack]
    max_len = max([len(s) for s in stack])
    return [s.ljust(max_len) for s in stack]

# given an list of strings, make a list of list of characters in each string
def stack_to_list(stack):
    return [list(s) for s in stack]

def get_stack_dict(fn,n=3):
    stack_matrix = np.array(stack_to_list(pad_right(head(fn,n=n))))

    stack_dict = {}
    for i,j in enumerate(np.arange(1,np.shape(stack_matrix)[1]-1,4)):
        stack_dict[i+1] = [s for s in ''.join(stack_matrix[:,j]).strip()]

    return stack_dict


def execute_instruction(stack_dict,instruction):
    n, from_arr, to_arr = instruction
    for _ in range(n):
        stack_dict[to_arr] = [stack_dict[from_arr][0]] + stack_dict[to_arr]
        stack_dict[from_arr] = stack_dict[from_arr][1:]
    return stack_dict

def parse_instructions(fn,n):
    instruction_list = tail(fn, n=n)
    return [[int(instruction.split()[1]),
             int(instruction.split()[3]),
             int(instruction.split()[5])] for instruction in instruction_list]

stack_dict = get_stack_dict('d05_test.txt',n=3)
for instruction in parse_instructions('d05_test.txt',n=5):
    stack_dict = execute_instruction(stack_dict,instruction)
    print(stack_dict)
top_stock = ''.join([stack_dict[k][0] for k in stack_dict.keys()])
assert top_stock == 'CMZ'

stack_dict = get_stack_dict('d05.txt',n=8)
for instruction in parse_instructions('d05.txt',n=10):
    stack_dict = execute_instruction(stack_dict,instruction)
    print(stack_dict)
top_stock = ''.join([stack_dict[k][0] for k in stack_dict.keys()])
print(f"Part 1: {top_stock}")

# Part 2
def execute_instruction_new(stack_dict,instruction):
    n, from_arr, to_arr = instruction
    stack_dict[to_arr] = stack_dict[from_arr][:n] + stack_dict[to_arr]
    stack_dict[from_arr] = stack_dict[from_arr][n:]
    return stack_dict

stack_dict = get_stack_dict('d05_test.txt',n=3)
for instruction in parse_instructions('d05_test.txt',n=5):
    stack_dict = execute_instruction_new(stack_dict,instruction)
    print(stack_dict)
top_stock = ''.join([stack_dict[k][0] for k in stack_dict.keys()])
assert top_stock == 'MCD'

stack_dict = get_stack_dict('d05.txt',n=8)
for instruction in parse_instructions('d05.txt',n=10):
    stack_dict = execute_instruction_new(stack_dict,instruction)
    print(stack_dict)
top_stock = ''.join([stack_dict[k][0] for k in stack_dict.keys()])
print(f"Part 2: {top_stock}")

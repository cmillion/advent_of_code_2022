# Day 1: Calorie Counting
import numpy as np

def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data

def find_loads(fn):
    d = read_file(fn)
    elves = [elf.split() for elf in d.split('\n\n')]
    return [np.array(elf,dtype='int').sum() for elf in elves]

loads = find_loads('d01_test.txt')
assert np.max(loads) == 24000
assert np.argmax(loads) == 4-1 # zero-indexed

assert np.sort(loads)[-3:].sum() == 45000

loads = find_loads('d01.txt')
print(f'Part 1: {np.max(loads)}')

print(f'Part 2: {np.sort(loads)[-3:].sum()}')

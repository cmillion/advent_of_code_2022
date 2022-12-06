# Day 4: Camp Cleanup
import numpy as np

def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data


# expand a range into a list of integers
def expand_range(r):
    start, end = r.split('-')
    return list(range(int(start), int(end)+1))


# determine whether one list of integers is a subset of another
def is_subset(subset, superset):
    return all([s in superset for s in subset])

def contains_subsets(filename):
    pairs = [[assignments.split(',') for assignments in data.split()][0] for data in read_file(filename).splitlines()]
    ranges = [[expand_range(pair[0]),expand_range(pair[1])] for pair in pairs]
    return [any([is_subset(r[0],r[1]),is_subset(r[1],r[0])]) for r in ranges]

assert sum(contains_subsets('d04/d04_test.txt')) == 2

print(f'Part 1: {sum(contains_subsets("d04/d04.txt"))}')

# determine whether two lists of integers have any elements in common
def has_overlap(r1, r2):
    return any([s in r2 for s in r1])

def contains_overlap(filename):
    pairs = [[assignments.split(',') for assignments in data.split()][0] for data in read_file(filename).splitlines()]
    ranges = [[expand_range(pair[0]),expand_range(pair[1])] for pair in pairs]
    return [any([has_overlap(r[0],r[1]),has_overlap(r[1],r[0])]) for r in ranges]

assert sum(contains_overlap('d04/d04_test.txt')) == 4

print(f'Part 2: {sum(contains_overlap("d04/d04.txt"))}')

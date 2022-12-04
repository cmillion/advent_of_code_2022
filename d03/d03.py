# Day 3: Rucksack Reorganization
import numpy as np

def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data

# split the string in half into a tuple
def split_string(data):
    half = int(len(data)/2)
    return (data[:half], data[half:])

# determine which characters in the first half of the string are in the second half using sets
def find_matches(pack):
    first, second = split_string(pack)
    matches = list(set(first).intersection(set(second)))
    assert len(matches)==1
    return matches[0]

def get_matches(filename):
    return [find_matches(pack) for pack in read_file(filename).split()]

# generate a string from a to z
def generate_alphabet():
    return ''.join([chr(i) for i in range(97,123)])

# generate a string from A to Z
def generate_alphabet_caps():
    return ''.join([chr(i) for i in range(65,91)])

def get_item_priority(item):
    priorities = generate_alphabet()+generate_alphabet_caps()
    return priorities.index(item)+1

def get_pack_priorities(pack):
    return [get_item_priority(item) for item in pack]

assert np.array(get_pack_priorities(get_matches('d03_test.txt'))).sum() == 157

print(f'Part 1: {np.array(get_pack_priorities(get_matches("d03.txt"))).sum()}')

# step through an array three items at a time
def step_through(filename):
    data = read_file(filename).split()
    return [data[i:i+3] for i in range(0,len(data),3)]

# determine which character is shared between three strings using sets
def find_shared_character(packs):
    first, second, third = packs
    shared = list(set(first).intersection(set(second), set(third)))
    assert len(shared)==1
    return shared[0]

def get_badges(filename):
    return [find_shared_character(packs) for packs in step_through(filename)]

def get_badge_priorities(badges):
    return [get_item_priority(item) for item in badges]

assert np.array(get_badge_priorities(get_badges('d03_test.txt'))).sum() == 70

print(f'Part 2: {np.array(get_badge_priorities(get_badges("d03.txt"))).sum()}')
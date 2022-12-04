# Day 2: Rock Paper Scissors
import numpy as np

def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data

def parse_strategy(fn):
    d = read_file(fn)
    strategy = [line.split() for line in d.split('\n')]
    return strategy

def score_play(round):
    play = round[1]
    return {'X': 1, 'Y': 2, 'Z': 3}[play]

def score_round(round):
    a,b=round
    if ((a=='A' and b=='X') or
        (a=='B' and b=='Y') or
        (a=='C' and b=='Z')): # draw
        return 3
    elif ((a=='A' and b=='Y') or
          (a=='B' and b=='Z') or
          (a=='C' and b=='X')): # win
        return 6
    else: # lose
        return 0

def score_match(strategy):
    return np.array([score_play(round)+score_round(round) for round in strategy]).sum()

strategy = parse_strategy('d02_test.txt')
assert score_match(strategy)==15

print('Part 1: ', score_match(parse_strategy('d02.txt')))

def play_strategy(round):
    a,b = round
    if b=='Y':
        return a,{'A': 'X', 'B': 'Y', 'C': 'Z'}[a]
    elif b=='X':
        return a,{'A': 'Z', 'B': 'X', 'C': 'Y'}[a]
    elif b=='Z':
        return a,{'A': 'Y', 'B': 'Z', 'C': 'X'}[a]

assert score_match([play_strategy(round) for round in strategy])==12
print(f'Part 2: {score_match([play_strategy(round) for round in parse_strategy("d02.txt")])}')

# Day 9 - Rope Bridge
import numpy as np
import itertools as it

def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

d = read_data('d09_test.txt')

def is_near(H,T):
    return abs(H[0]-T[0])<=1 and abs(H[1]-T[1])<=1

def simulate(d):
    i, j = 0, 0  # position of head
    m, n = 0, 0  # position of tail
    tail_has_been = []
    for move in d.split('\n'):
        #print(move)
        for _ in range(int(move.split(' ')[1])):
            if move[0]=='U':
                i+=1
                if not is_near((i,j),(m,n)):
                    n=j
                    m+=1
            if move[0]=='D':
                i-=1
                if not is_near((i,j),(m,n)):
                    n=j
                    m-=1
            if move[0]=='R':
                j+=1
                if not is_near((i,j),(m,n)):
                    m=i
                    n+=1
            if move[0]=='L':
                j-=1
                if not is_near((i,j),(m,n)):
                    m=i
                    n-=1
            # update unique locations list
            if not [n,m] in tail_has_been:
                tail_has_been+=[[n,m]]
            #print(i,j,m,n)
            #print()
    return tail_has_been

assert len(simulate(d))==13

d = read_data('d09.txt')
print(f'Part 1: {len(simulate(d))}')
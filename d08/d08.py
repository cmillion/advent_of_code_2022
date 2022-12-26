# Day 8: Treetop Tree House
import numpy as np
import itertools as it

# read in the data
def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

fn = 'd08_test.txt'
data = read_data(fn)
f = np.array([[col for col in row] for row in data.split()],dtype='int32')

def visible_trees(f):
    from_the_left = np.array([[all(row[:i]<tree) for i,tree in enumerate(row)] for row in f])
    from_the_right = np.fliplr([[all(row[:i]<tree) for i,tree in enumerate(row)] for row in np.fliplr(f)])
    from_the_top = np.rot90([[all(row[:i]<tree) for i,tree in enumerate(row)] for row in np.rot90(f)],k=3)
    from_the_bottom = np.rot90([[all(row[:i]<tree) for i,tree in enumerate(row)] for row in np.rot90(f,k=3)],k=1)

    return from_the_left+from_the_right+from_the_top+from_the_bottom

assert np.sum(visible_trees(f))==21

fn = 'd08.txt'
data = read_data(fn)
f = np.array([[col for col in row] for row in data.split()],dtype='int32')

print(f"Part 1: {np.sum(visible_trees(f))}")

def get_view(r,t):
    for i,j in enumerate(r):
        if j>=t:
            return i+1
    return len(r)

def find_max_view(f):
    views = []
    for i,j in it.product(range(np.shape(f)[0]),range(np.shape(f)[1])):
        tree = f[i,j]

        try:
            dn = get_view(f[i+1:,j],tree)
        except IndexError:
            dn = 0

        try:
            up = get_view(f[:i,j][::-1],tree)
        except IndexError:
            up = 0

        try:
            rt =get_view(f[i,j+1:],tree)
        except IndexError:
            rt = 0

        try:
            lt = get_view(f[i,:j][::-1],tree)
        except IndexError:
            lt = 0

        views+=[np.product([dn,up,rt,lt])]
    return max(views)

fn = 'd08_test.txt'
data = read_data(fn)
f = np.array([[col for col in row] for row in data.split()],dtype='int32')
assert find_max_view(f)==8

fn = 'd08.txt'
data = read_data(fn)
f = np.array([[col for col in row] for row in data.split()],dtype='int32')
print(f"Part 2: {find_max_view(f)}")

# 249480 is too low
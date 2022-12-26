# Day 7: No Space Left On Device

def read_file(filename):
    with open(filename) as f:
        data = f.read()
    return data

data = read_file('d07_test.txt')
commands = data.split('\n')

print(commands)
# Day 6: Tuning Trouble

ex1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# find the first four adjacent characters in a string that are all different from each other
# return the index of the last character in the substring
def find_adjacent(s,n=4):
    for i in range(len(s)-n-1):
        if len(set(s[i:i+n]))==n:
            return i+n # zero indexed, so add 1
    return None

assert find_adjacent("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert find_adjacent("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert find_adjacent("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert find_adjacent("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert find_adjacent("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

# read the input file
with open('d06.txt') as f:
    data = f.read().strip()

print(f'Part 1: {find_adjacent(data)}')

assert find_adjacent("mjqjpqmgbljsphdztnvjfqwrcgsmlb",n=14) == 19
assert find_adjacent("bvwbjplbgvbhsrlpgdmjqwftvncz",n=14) == 23
assert find_adjacent("nppdvjthqldpwncqszvftbrmjlhg",n=14) == 23
assert find_adjacent("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",n=14) == 29
assert find_adjacent("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",n=14) == 26

print(f'Part 2: {find_adjacent(data,n=14)}')

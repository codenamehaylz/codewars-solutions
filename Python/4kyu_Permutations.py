# So Many Permutations!
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

# Create all permutations of a non-empty input string and remove duplicates
# Order doesn't matter

import itertools

def permutations(s):
    perms = itertools.permutations(s)
    shufflings = set()
    for i in perms:
        shufflings.add(''.join(i))
    return shufflings

print(permutations("aabb"))
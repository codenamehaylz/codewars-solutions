# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# Examples:
# 'abc' =>  ['ab', 'c_']
# 'abcdef' => ['ab', 'cd', 'ef']


#* My Solution!

def solution(s):
    pairs = []
    if len(s) % 2 != 0:
        s += '_'
    for i in range(0, len(s), 2):
        pair = s[i] + s[i+1]
        pairs.append(pair)
    return pairs
        
print(solution('abcde'))


#* My favourite solution from others!

import re

def other_solution(s):
    return re.findall(".{2}", s + "_")

print(other_solution('abcde'))
# Friend or Foe?
# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

# Filter a list of strings to find names of exactly 4 letters
# Return a list
# Keep original order


# def friend(x):

#     def findFriends(name):
#         if len(name) == 4:
#             return True
#         else:
#             return False
        
#     friends = filter(findFriends, x)
#     return list(friends)


def friend(x):
    return [name for name in x if len(name) == 4]

print(friend(["Ryan", "Kieran", "Mark",]))

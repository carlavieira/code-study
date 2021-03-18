""""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""
def isUnique(string):
    if len(string) > 128: return False;
    char_set = set()
    for char in string:
        if char in char_set: return False
        char_set.add(char)
    return True

print(isUnique('asdf'))
print(isUnique('asdfa'))
print(isUnique('asdfdsad'))
print(isUnique('asqwodf'))
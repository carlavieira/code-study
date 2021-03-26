def is_unique(string):
    char_set = set()
    for char in string:
        if char in char_set: return False
        char_set.add(char)
    return True

def is_unique_without_data_structures(string):
    string = sorted(string)
    for index in range(len(string)-1):
        if string[index] == string[index+1]: return False
    return True

print(is_unique("abcdef"))
print(is_unique("abcdefa"))
print(is_unique_without_data_structures("abcdef"))
print(is_unique_without_data_structures("abcdefa"))
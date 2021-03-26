def check_permutation(string1, string2):
    if len(string1) != len(string2): return False
    char_dict1 = {}
    char_dict2 = {}
    for char in string1:
        char_dict1[char] = char_dict1[char] + 1 if char in char_dict1 else 1
    for char in string2:
        char_dict2[char] = char_dict2[char] + 1 if char in char_dict2 else 1
    if char_dict1.keys() != char_dict2.keys(): return False
    for char, value1 in char_dict1.items():
        if value1 != char_dict2[char]: return False
    return True

print(check_permutation("abab", "bbaa"))
print(check_permutation("abab", "bbaac"))
print(check_permutation("abab", "bbac"))
print(check_permutation("abab", "bbaaa"))
print(check_permutation("bbbbccc", "bcbcbcb"))
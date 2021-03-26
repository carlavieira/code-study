def string_rotation(straing1, string2):
    if len(straing1) == len(string2) and straing1:
        string3= straing1+straing1
        return is_substring(string3, string2)
    return False

def is_substring(string1, string2):
    return string2 in string1

print(string_rotation("abcdef", "efabcd"))
print(string_rotation("abcdef", "efabcf"))
def palindrome_permutation(string):
    char_dict = {}
    string_chars = list(string.lower().replace(" ", ""))
    for char in string_chars:
        char_dict[char] = char_dict[char] + 1 if char in char_dict else 1
    is_first_letter = True
    for value in char_dict.values():
        if value % 2 != 0:
            if is_first_letter:
                is_first_letter = False
            else:
                return False
    return True

def palindrome_permutation_better(string):
    char_dict = {}
    count_odd = 0
    string_chars = list(string.lower().replace(" ", ""))
    for char in string_chars:
        char_dict[char] = char_dict[char] + 1 if char in char_dict else 1
        if char_dict[char] % 2:
            count_odd +=1
        else:
            count_odd -=1
    return count_odd <=1

print(palindrome_permutation("assnssa"))
print(palindrome_permutation("assntsa"))
print(palindrome_permutation("assnssa aa"))
print(palindrome_permutation("assnssa AAaa"))
print(palindrome_permutation("assnssa N"))

print(palindrome_permutation_better("assnssa"))
print(palindrome_permutation_better("assntsa"))
print(palindrome_permutation_better("assnssa aa"))
print(palindrome_permutation_better("assnssa AAaa"))
print(palindrome_permutation_better("assnssa N"))
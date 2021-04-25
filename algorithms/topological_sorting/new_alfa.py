from collections import defaultdict

def new_alpha(words):
    def topological_sort_util(letter, stack, seen):
        if letter not in seen:
            seen.add(letter)
            if letter in dict_letters:
                for child in dict_letters[letter]:
                    if child not in seen:
                        topological_sort_util(child, stack, seen)
            stack.append(letter)
            return stack


    dict_letters = defaultdict(list)
    for wi in range(len(words)-1):
        ci = 0
        word1 = words[wi].upper()
        word2 = words[wi+1].upper()
        while word1[ci] == word2[ci]:
            ci +=1
        dict_letters[word1[ci]].append(word2[ci])
    seen = set()
    stack = []

    for char in dict_letters:
        if char not in seen:
            topological_sort_util(char, stack, seen)

    return stack[::-1]

words=["ZZA", "ZZDC", "DAZ", "DAA", "C"]

print(new_alpha(words))

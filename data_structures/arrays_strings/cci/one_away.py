def is_one_away(string1, string2):
    if len(string1) == len(string2):
        return is_replace(string1, string2)
    elif len(string1) == len(string2) + 1:
        return is_insertion(string1, string2)
    elif len(string1) == len(string2) - 1:
        return is_insertion(string2, string1)
    else: return False

def is_replace(string1, string2):
    found_replace = False
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            if found_replace: return False
            else:
                found_replace = True
    return True

def is_insertion(string1, string2):
    #string2 should have one char more than string1
    index1 = index2 = 0
    while index2 < len(string2):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            else:
                index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

print(is_one_away("tes", "test"))
print(is_one_away("tes", "teste"))
print(is_one_away("tes", "tet"))
print(is_one_away("tes", "ts"))
print(is_one_away("tesdsg", "tsfdsf"))
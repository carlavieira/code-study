def sort_group_amagrams(arr):
    dict_sorted_strings = {}

    for string in arr:
        chars_sorted = sort_chars(string)
        if chars_sorted in dict_sorted_strings:
            new_list = dict_sorted_strings[chars_sorted]
            new_list.append(string)
        else:
            dict_sorted_strings[chars_sorted] = [string, ]

    index = 0
    for key, strings in dict_sorted_strings.items():
        for string in strings:
            arr[index] = string
            index +=1

    return arr

def sort_chars(string):
    char_list = list(string)
    char_list.sort()
    string = "".join(char_list)
    return string

arr = ["asa","bnb" , "oho" , "bbn", "ooh", "aas"]
print(sort_group_amagrams(arr))
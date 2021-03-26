def replace_spaces(string):
    return string.strip().replace(" ", "%20")

def replace_space_without_replace(string, true_len):
    num_of_spaces = count_of_chars(string, 0 , true_len, " ")
    string = list(string)
    pointer = len(string)-1
    for index in range(true_len-1, -1, -1):
        if string[index] == " ":
            string[pointer], string[pointer-1], string[pointer-2] = '0', '2', '%'
            pointer -= 3
        else:
            string[pointer] = string[index]
            pointer -= 1
    string = "".join(string)
    return string

def count_of_chars(string, start , end, char):
    count = 0
    for i in range(start, end):
        if string[i] == char:
            count += 1
    return count


string = "teste teste teste    "
print(replace_space_without_replace(string, 17))
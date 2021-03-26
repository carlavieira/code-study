def string_compression(string):
    final_len = count_compression(string)
    if final_len >= len(string): return string
    compressed = []
    counter = 0
    for index in range(len(string)):
        counter += 1
        if index >= len(string) -1 or string[index] != string[index+1]:
            compressed.append(string[index])
            compressed.append(str(counter))
            counter = 0
    return ''.join(compressed)

def count_compression(string):
    compressed_len = counter = 0
    for index in range(len(string)):
        counter += 1
        if index >= len(string) -1 or string[index] != string[index + 1]:
            compressed_len += 1 + len(str(counter))
            counter = 0
    return compressed_len

print(string_compression("aabcccccaaa"))
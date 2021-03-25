def sorted_merge(a, b, size_a):
    index_a = size_a - 1
    index_b = len(b) - 1
    index_current = len(a) -1

    while index_b >= 0:
        print("index_current ={}, index_a={}, index_b={}".format(index_current, index_a, index_b))
        print(" comparando a[{}] >= b[{}] -> {} >= {} -> {}".format(index_a, index_b,a[index_a],b[index_b], a[index_a] >= b[index_b]))
        if a[index_a] >= b[index_b] and index_a>=0:
            print("a[{}] recebe o valor de a[{}], que é {}".format(index_current,  index_a, a[index_a]))
            a[index_current] = a[index_a]
            index_a -= 1
        else:
            print("a[{}] recebe o valor de b[{}], que é {}".format(index_current,  index_b, b[index_b]))
            a[index_current] = b[index_b]
            index_b -= 1
        index_current -= 1

    return a

a = [1, 2, 4, 6, 7, 9, None ,None , None,None,None,None, None, None]
b = [3,5,6,7,8,12, 123,432]
print(sorted_merge(a, b, 6))
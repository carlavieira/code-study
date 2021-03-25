def sortedsearch_nosize(arr, target):
    index = 1
    while arr[index] != -1 and arr[index] < target:
        index *=2

    return binary_search(arr, 0, index, target)


def binary_search(arr, low, high, target):

    mid = high + low // 2

    if arr[mid] == target: return mid
    if target < arr[mid]:
        return binary_search(arr, low, mid-1, target)
    else:
        return binary_search(arr, mid +1, high, target)


print(sortedsearch_nosize([0, 1, 2, 3, 3,4, 5,231, 7642], 231))
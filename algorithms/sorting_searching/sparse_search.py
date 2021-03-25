def sparse_search(arr, string):
    if not arr or not string: return -1
    return recursive_binary_search(arr, string, 0, len(arr)-1)

def recursive_binary_search(arr, string, first, last):
    if first > last: return -1

    mid = (first + last) // 2

    #that is not midd, find the closest nonempty value
    if not arr[mid]:
        # set pointers do mid side
        left = mid - 1
        right = mid + 1
        while True:
            #  if gets to the point that the pointers exceed the perimeters, that is not a valid value
            if left < first and right > last:
                return -1
            elif arr[right] and right <= last:
                mid = right
                break
            elif arr[left] and left >= first:
                mid = left
                break
            left -= 1
            right += 1
            
            
    if arr[mid] == string: return mid
    elif arr[mid] > string: return recursive_binary_search(arr, string, first, mid-1)
    elif arr[mid] < string: return recursive_binary_search(arr, string, mid + 1, last)


arr=['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
print(sparse_search(arr, "ball"))
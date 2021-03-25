def search_rotated_array(arr, target):
    return search_rotated_array_recusrsive(arr, 0, len(arr)-1, target)

def search_rotated_array_recusrsive(arr, left, right, target):
    if (right < left): return -1

    mid = (left + right) // 2

    if target == arr[mid]: return mid

    if arr[left] < arr[mid]: #if the left subarr its normally ordered
        if arr[left] <= target and target < arr[mid]: #if the target its in the left subarray
            return search_rotated_array_recusrsive(arr, left, mid-1, target)
        else:
            return search_rotated_array_recusrsive(arr, mid + 1, right, target)
    elif arr[mid] < arr[right]: #if the right subarr its normally ordered
        if arr[mid] < target and target <=arr[right]: #if the target its in the right subarray
            return search_rotated_array_recusrsive(arr, mid + 1, right, target)
        else:
            return search_rotated_array_recusrsive(arr, left, mid - 1, target)
    else:
        location = -1
        if arr[left] == arr[mid]: # if arr[left] == arr[mid], it will search in the right subarray
            location  = search_rotated_array_recusrsive(arr, mid + 1, right, target)
        if location == -1 and arr[mid] == arr[right]: # if arr[left] != arr[mid] or if it couldn't find in the right arr and arr[left] == arr[mid]
            location = search_rotated_array_recusrsive(arr, left, mid - 1, target)
        return location

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search_rotated_array(arr, 5))
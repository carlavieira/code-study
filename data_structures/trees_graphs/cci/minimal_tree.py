class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def minimal_tree(arr_int):
    def recursive_add(start, end):
        if start == end:
            return Node(arr_int[start])
        mid = (start+end) // 2
        new_node = Node(arr_int[mid], [recursive_add(start, mid-1), recursive_add(mid+1, end)])
        return new_node

    root = recursive_add(0, len(arr_int)-1)

    return root
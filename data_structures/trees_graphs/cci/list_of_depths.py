class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_of_depth(root):
    def add_pre_order(root, lists_of_depth, depth):
        if root:
            #visit node
            if lists_of_depth[depth]:
                lists_of_depth[depth] = ListNode(root.val, lists_of_depth[depth])
            else:
                lists_of_depth.append(ListNode(root.val, None))
            # go to left
            add_pre_order(root.left, lists_of_depth, depth+1)
            # got to right
            add_pre_order(root.right, lists_of_depth, depth+1)

    lists_of_depth = []
    add_pre_order(root, lists_of_depth, 0)
    return lists_of_depth
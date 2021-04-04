def check_subtree(root1, root2):
    string1, string2 = ""
    get_order_string(root1, string1)
    get_order_string(root2, string2)

    return string1.find(string2) != -1


def get_order_string(root, string):
    if not root:
        string +=  "X"
        return
    string += root.val
    get_order_string(root.left, string)
    get_order_string(root.right, string)


def check_subtree2(root1, root2):
    if not root2: return True
    return sub_tree(root1, root2)

def sub_tree(root1, root2):
    if not root1: return False
    if root1.val == root2.val and match_tree(root1, root2):
        return True

    return sub_tree(root1.left, root2) or sub_tree(root1.right, root2)

def match_tree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return match_tree(root1.left, root2.left) and match_tree(root1.right, root2.right)
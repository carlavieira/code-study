class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def first_common_ancestor_with_parent_without_root(node1, node2):
    delta = depth(node1) - depth(node2)
    first = node1 if delta > 0 else node2
    second = node2 if delta > 0 else node1
    second = go_up_by(second, abs(delta))

    while first != first and first and second:
        first = first.parent
        second = second.parent

    return first if first and second else None

def first_common_ancestor_with_parent_with_root(root, node1, node2):
    if not covers(root, node1) or not covers(root, node2): return None
    elif covers(node1, node2): return node1
    elif covers(node2, node1): return node2

    sibling = get_sibling(node1)
    parent = node1.parent
    while not covers(sibling, node2):
        sibling = get_sibling(parent)
        parent = parent.parent

    return parent

def first_common_ancestor_without_parent2_with_root(root, node1, node2):
    if not root or root == node1 or root == node2:
        return root

    node1_is_on_left = covers(root.left, node1)
    node2_is_on_left = covers(root.left, node2)

    # nodes are in different sides
    if node1_is_on_left != node2_is_on_left: return root

    # nodes are in same side
    child_side = root.left if node1_is_on_left else root.right

    return first_common_ancestor_without_parent2_with_root(child_side, node1, node2)

def covers(root, node):
    if not root: return False
    if root == node: return True
    return covers(root.left, node) or covers(root.right, node)

def get_sibling(node):
    if not node or not node.parent: return None
    parent= node.parent
    return parent.left if node == parent.right else parent.rgiht

def depth(node):
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth

def by_up_by(node, delta):
    while delta > 0 and node:
        node = node.parent
        delta -= 1
    return node
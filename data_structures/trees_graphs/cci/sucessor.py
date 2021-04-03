class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

def sucessor(node):
    if not node: return None

    if node.right:
        while node.left:
            node = node.left
    else:
        parent = node.parent
        while node and parent.left != node:
            node = parent
            parent = node.parent
    return node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validate_bst(root):
    if not root:
        return True
    if not validate_bst(root.left) or not validate_bst(root.right):
        return False
    return root.left.val <= root.val and root.right.val > root.val
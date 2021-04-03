class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balenced(root):
    def get_height(node):
        if not node.left and not node.right:
            return 0
        left_height = get_height(node.left)if node.left else 0
        right_height = get_height(node.right) if node.right else 0
        return max(left_height+1,right_height+1)

    if not root:
        return True
    height = get_height(root.left)-get_height(root.right)
    if abs(height) > 1:
        return False
    return is_balenced(root.left) and is_balenced(root.right)
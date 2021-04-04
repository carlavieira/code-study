import random

class Tree:
    def __init__(self):
        self.root=None
        self.size=0

    def get_random_node(self):
        if not self.root: return None
        index = random.randrange(self.size)
        return self.root.getIthNode(index)

    def insertInOrder(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.root.insert_in_order(value)

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1

    def get_ith_node(self, index):
        left_size = 0 if not self.left else self.left.size
        if index < left_size:
            return self.left.get_ith_node(index)
        elif index == left_size:
            return self
        else:
             return self.right.get_ith_node(index-(left_size+1))

    def insert_in_order(self, value):
        if value <= self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insert_in_order(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insert_in_order(value)
        self.size += 1

    def find(self, value):
        if value == self.value:
            return self
        elif value < self.value:
            return self.left.find(value) if self.left else None
        else:
            return self.right.find(value) if self.right else None
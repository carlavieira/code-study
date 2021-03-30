class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_middle_node(node):
    if not node or not node.next: raise Exception("Invalid. LinkedList empty or last node given")
    node.val = node.next.val
    node.next = node.next.next
    return True

node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)

pointer = node4
while pointer:
    print(pointer.val)
    pointer = pointer.next

delete_middle_node(node3)

pointer = node4
while pointer:
    print(pointer.val)
    pointer = pointer.next
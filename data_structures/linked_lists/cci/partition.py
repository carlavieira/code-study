class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(node, x):
    head = tail = node
    while node:
        next = node.next
        if node.val < x:
            #insert node at head
            node.next = head
            head=node
        else:
            #insert node at tail
            tail.next = node
            tail=node
        node = next
    tail.next = None

    return head


node1 = ListNode(5)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)

pointer = node4
while pointer:
    print(pointer.val)
    pointer = pointer.next

node4= partition(node4, 3)

pointer = node4
while pointer:
    print(pointer.val)
    pointer = pointer.next
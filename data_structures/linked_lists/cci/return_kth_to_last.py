class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def return_kth_to_last(head, k):
    pointer1 = pointer2 = head

    for i in range(k):
        if not pointer1: return None
        pointer1=pointer1.next

    while pointer1:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer2

node1 = ListNode(4)
node2 = ListNode(23, node1)
node3 = ListNode(32, node2)
node4 = ListNode(1, node3)
print(return_kth_to_last(node4, 2).val)

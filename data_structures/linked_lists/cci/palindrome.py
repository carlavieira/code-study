class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(node):
    pointer_fast = pointer_slow = node

    stack = []

    while pointer_fast and pointer_fast.next:
        stack.append(pointer_slow.val)
        pointer_slow = pointer_slow.next
        pointer_fast = pointer_fast.next.next

    if pointer_fast:
        pointer_slow = pointer_slow.next

    while pointer_slow:
        top = stack.pop()
        if top != pointer_slow.val:
            return False
        pointer_slow = pointer_slow.next

    return True


node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(2, node3)
node5 = ListNode(1, node4)
print(is_palindrome(node5))
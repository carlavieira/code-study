class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def loop_detection(node):
    pointer_slow = pointer_fast = node

    while pointer_fast and pointer_fast.next:
        pointer_slow = pointer_slow.next
        pointer_fast = pointer_fast.next
        if pointer_slow == pointer_fast:
            break

    if not pointer_fast or not pointer_fast.next:
        return None

    pointer_slow=node
    while pointer_slow != pointer_fast:
        pointer_slow = pointer_slow.next
        pointer_fast = pointer_fast.next

    return pointer_fast
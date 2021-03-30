class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    debt = 0
    list_sum = []
    pointer1, pointer2 = l1, l2
    while pointer1 and pointer2:
        sum_digits = pointer1.val + pointer2.val + debt
        debt = 0
        if sum_digits >= 10:
            debt = sum_digits // 10
            sum_digits = sum_digits % 10
        list_sum.append(sum_digits)
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    while pointer1:
        sum_digits = pointer1.val + debt
        debt = 0
        if sum_digits >= 10:
            debt = sum_digits // 10
            sum_digits = sum_digits % 10
        list_sum.append(sum_digits)
        pointer1 = pointer1.next
    while pointer2:
        sum_digits = pointer2.val + debt
        debt = 0
        if sum_digits >= 10:
            debt = sum_digits // 10
            sum_digits = sum_digits % 10
        list_sum.append(sum_digits)
        pointer2 = pointer2.next
    if debt:
        list_sum.append(debt)
    pointer3 = None
    for dig in list_sum[::-1]:
        pointer3 = ListNode(dig, pointer3)
    return pointer3
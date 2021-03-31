class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def intersection(node1, node2):
    set_nodes_list1 = set()
    set_nodes_list2 = set()

    while node1 and node2:
        if node1 == node2:
            return node1
        if node1 in set_nodes_list2:
            return node1
        if node2 in set_nodes_list1:
            return node2
        set_nodes_list1.add(node1)
        set_nodes_list2.add(node2)
        node1 = node1.next
        node2 = node2.next

    while node1:
        if node1 in set_nodes_list2:
            return node1
        node1 = node1.next

    while node2:
        if node2 in set_nodes_list1:
            return node2
        node2 = node2.next

    return None

node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)

node5 = ListNode(5, node1)
node6 = ListNode(6, node5)

print(intersection(node4, node5).val)
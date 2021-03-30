class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_dups(llnode: ListNode):
    nodes_values = set()
    previous_node = None
    while llnode:
        if llnode.val in nodes_values:
            previous_node.next = llnode.next
        else:
            nodes_values.add(llnode.val)
            previous_node = llnode
        llnode = llnode.next

node1 = ListNode(4)
node2 = ListNode(3, node1)
node3 = ListNode(3, node2)
node4 = ListNode(1, node3)
remove_dups(node4)
pointer = node4
while pointer:
    print(pointer.val)
    pointer = pointer.next
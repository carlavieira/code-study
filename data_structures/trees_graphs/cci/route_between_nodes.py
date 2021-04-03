from collections import deque

class Graph:
    def __init__(self, nodes=None):
        self.nodes = nodes


class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        self.marked_start = False
        self.marked_end = False

def route_between_nodes(node_start, node_end) -> bool:
    nodes_queue = deque()
    node_start.marked_start = True
    nodes_queue.append(node_start)
    while nodes_queue:
        actual_node = nodes_queue.popleft()
        if actual_node == node_end:
            return True
        for child in actual_node.children:
            if not child.marked_start:
                child.marked_start = True
                nodes_queue.append(child)
    return False


def route_between_nodes_undirected(node_start, node_end) -> bool:
    queue_start, queue_end = deque(), deque()
    node_start.marked_start = True
    node_end.marked_end = True
    queue_start.append(node_start)
    queue_end.append(node_end)
    while queue_start or queue_end:
        actual_node_start = queue_start.popleft()
        actual_node_end = queue_end.popleft()
        if actual_node_start.marked_end or actual_node_end.marked_start:
            return True
        for child in actual_node_start.children:
            if not child.marked:
                child.marked_start = True
                queue_start.append(child)
        for child in actual_node_end.children:
            if not child.marked:
                child.marked_end = True
                queue_end.append(child)
    return False

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.children = [node2, node3]
node3.children = [node4]
node4.children = [node5, node6]
node6.children = [node7]
print(route_between_nodes(node1, node7))
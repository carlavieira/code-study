""""
Part 4: Linked Lists

A linked list is a linear collection of data elements, whose order is not given by their physical placement in
memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which
together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words,
a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from
any position in the sequence during iteration.

Implement a Singly Linked List class with the following methods:
* void push(<Node> node) → Adds the node to the end of the list
* <Node> pop() → Removes the last node at the end of the linked list, returns that data
* void insert(uint index,<Node> node) → Adds a single node containing data to a chosen location in the list. If the
index is above the size of the list, do nothing
* void remove(uint index) → remove/delete a single node at the index location in the list. If the node doesn’t exist at
the index, do nothing
* <Node> elementAt(uint index) → Returns a pointer to the node at the index location in the list. If the node doesn’t
exist at the index, return nil/null
* uint size() → Returns the length of the list.
* void printList() → Returns a string representation of the linked list

Tips:
 - First define your Node (contains a data element of integer type, and a next-node element that is a node-pointer).
 - Then define a Linked List that links the nodes as per the above methods.
 - Implement the following tests (should be self explanatory):
        - testPushBackAddsOneNode
        - testPopBackRemovesCorrectNode
        - testEraseRemovesCorrectNode
        - testEraseDoesNothingIfNoNode
        - testElementAtReturnNode
        - testElementAtReturnsNoNodeIfIndexDoesNotExist
        - testSizeReturnsCorrectSize

In a Linked List, a “cycle” occurs if a given node in the Linked List references an earlier node for its “next”
reference. Add a method to your Linked List called hasCycle() which returns a boolean denoting whether a cycle exists.

Bonus
Implement a function to check if a linked list is a palindrome.

"""
from math import ceil, floor

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, node: Node):
        if not self.head: self.head = node
        else:
            mark = self.cycleMark() if self.hasCycle() else None
            pointer = self.head
            is_first_time = True
            while pointer.next:
                if pointer.next == mark:
                    if is_first_time:
                        is_first_time = False
                    else:
                        break
                pointer = pointer.next
            pointer.next = node
        self.size += 1

    def pop(self):
        if not self.head: raise Exception("Empty Linked List")
        mark = self.cycleMark() if self.hasCycle() else None
        pointer = self.head
        if pointer.next == mark:
            delete_node = self.head
            self.head = None
        else:
            is_first_time = True
            while pointer:
                if pointer.next == mark:
                    if is_first_time:
                        is_first_time = False
                    else:
                        break
                previous_node = pointer
                pointer = pointer.next
            delete_node = pointer
            previous_node.next = mark
        self.size -= 1
        return delete_node


    def insert(self, index: int, node: Node):
        if index > self.size-1 or index < 0: return
        pointer = self.head
        for x in range(index-1):
            pointer = pointer.next
        node.next = pointer.next
        pointer.next = node
        self.size += 1

    def remove(self, index: int):
        if index > self.size-1 or index < 0: return
        pointer = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for x in range(index):
                previous_node = pointer
                pointer = pointer.next
            previous_node.next = pointer.next
        self.size -= 1

    def elemntAt(self, index: int):
        if index > self.size-1 or index < 0: None
        pointer = self.head
        for x in range(index):
            pointer = pointer.next
        return pointer

    def sizeN(self):
        if not self.head: return 0
        counter = 0
        mark = self.cycleMark() if self.hasCycle() else None
        pointer = self.head
        is_first_time = True
        while pointer:
            if pointer == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            counter += 1
            pointer = pointer.next
        return counter

    def size1(self):
        return self.size

    def printList(self):
        print("Linked List: [ ", end="")
        if self.size == 0:
            print("]")
            return
        mark = self.cycleMark() if self.hasCycle() else None
        pointer = self.head
        is_first_time = True
        while pointer:
            if pointer == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            print(pointer.value, end=" -> ")
            pointer = pointer.next
        print(pointer.value if pointer else None, end="")
        print(" ]")

    def hasCycle(self):
        if not self.head: raise Exception("Empty Linked List")
        set_nodes = set()
        pointer = self.head
        while pointer:
            if pointer in set_nodes:
                return True
            set_nodes.add(pointer)
            pointer = pointer.next
        return False

    def cycleMark(self):
        if not self.head: raise Exception("Empty Linked List")
        set_nodes = set()
        pointer = self.head
        while pointer:
            if pointer in set_nodes:
                return pointer
            set_nodes.add(pointer)
            pointer = pointer.next
        return None

    def isPalindrome(self):
        mark = self.cycleMark() if self.hasCycle() else None
        pointer = self.head
        list_values = []
        is_first_time = True
        while pointer:
            if pointer == mark:
                if is_first_time:
                    is_first_time = False
                else:
                    break
            list_values.append(pointer.value)
            pointer = pointer.next
        return list_values[:len(list_values)//2] == list_values[len(list_values):ceil(len(list_values)/2)-1:-1]

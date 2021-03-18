""""
Part 4: Linked Lists

A linked list is a linear collection of data elements, whose order is not given by their physical placement in
memory. Instead, each element points to the next. It is a data structure consisting of a collection of nodes which
together represent a sequence. In its most basic form, each node contains: data, and a reference (in other words,
a link) to the next node in the sequence. This structure allows for efficient insertion or removal of elements from
any position in the sequence during iteration.

Implement a Singly Linked List class with the following methods:
* void push(<Node> node) → Adds the node to the end othe list
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

class SinglyLinkedList:

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __index__(self):
        self.top=None


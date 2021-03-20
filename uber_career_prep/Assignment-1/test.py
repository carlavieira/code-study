from Part2 import *
from Part3 import *
from Part4 import *
from Part5 import *
import unittest

class TestPart2(unittest.TestCase):

    def test_isStringPermutation(self):
        self.assertTrue(isStringPermutation('asdf', 'fsda'))
        self.assertFalse(isStringPermutation('asdf', 'fsa'))
        self.assertFalse(isStringPermutation('asdf', 'fsax'))

    def test_pairsThatEqualSum(self):
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5], 5), [(2, 3), (1, 4)])
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5], 1), [])
        self.assertEqual(pairsThatEqualSum([1, 2, 3, 4, 5], 7), [(3, 4), (2, 5)])

class TestPart3(unittest.TestCase):

    def test_Stack(self):
        myStack = Stack()
        myStack.push(42)
        self.assertEqual(myStack.top(), 42)
        self.assertEqual(myStack.size1(), 1)
        self.assertFalse(myStack.isEmpty())
        popped_value = myStack.pop()
        self.assertEqual(popped_value, 42)
        self.assertEqual(myStack.size1(), 0)
        self.assertTrue(myStack.isEmpty(), True)
        myStack.push(42)
        self.assertRaises(TypeError, myStack.push, "carla")
        myStack.pop()
        myStack.push("carla")
        myStack.push("maria")
        self.assertEqual(myStack.size1(), 2)
        self.assertEqual(myStack.top(), "maria")

    def test_Queue(self):
        myQueue = Queue()
        myQueue.enqueue(1)
        myQueue.enqueue(2)
        myQueue.enqueue(3)
        self.assertEqual(myQueue.size1(), 3)
        self.assertEqual(myQueue.front(), 1)
        self.assertEqual(myQueue.rear(), 3)
        dequeuedItem = myQueue.dequeue()
        self.assertEqual(dequeuedItem, 1)
        self.assertEqual(myQueue.size1(), 2)
        myQueue.enqueue("carla")
        self.assertEqual(myQueue.rear(), "carla")

class TestPart4(unittest.TestCase):

    def testPushBackAddsOneNode(self):
        myLList = SinglyLinkedList()
        myLList.push(Node(1))
        self.assertEqual(myLList.sizeN(), 1)
        self.assertEqual(myLList.size1(), 1)
        myLList.push(Node(2))
        self.assertEqual(myLList.sizeN(), 2)
        self.assertEqual(myLList.size1(), 2)
        myLList.push(Node(3, myLList.head))
        self.assertEqual(myLList.sizeN(), 3)
        self.assertEqual(myLList.size1(), 3)


    def testPopBackRemovesCorrectNode(self):
        pass
    def testEraseRemovesCorrectNode(self):
        pass
    def testEraseDoesNothingIfNoNode(self):
        pass
    def testElementAtReturnNode(self):
        pass
    def testElementAtReturnsNoNodeIfIndexDoesNotExist(self):
        pass
    def testSizeReturnsCorrectSize(self):
        pass

class TestPart5(unittest.TestCase):
    pass

        # myLinkedList = SinglyLinkedList()
        # myLinkedList.push(Node(1))
        # myLinkedList.push(Node(2))
        # myLinkedList.push(Node(3))
        # reversedLinkedList = reverseLinkedListIterative(myLinkedList)
        # myLinkedList.printList()
        # reversedLinkedList.printList()

if __name__ == '__main__':
    unittest.main()

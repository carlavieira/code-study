"""
Part 3: Stacks and Queues

Stacks

A stack is a container of objects that are inserted and removed according to the last-in first-out (LIFO) principle. In
“pushdown stacks” only two operations are allowed: push the item onto the top of the stack, and pop the item off of the
top of the stack. A stack is a limited access data structure - elements can be added and removed from the stack only at
the top. (Hence the name Stack, cause you stack items on top, and remove from the top.) A helpful analogy is to think of
 a stack of books; you can remove only the top book, also you can add a new book on the top.

Challenge: Implement the Stack class from scratch (do not use your language’s standard stack or queue library/package
methods). In this challenge, your Stack will only accept Integer values.

Implement the following methods:
    - push() → Pushes an integer on top of the stack
    - pop() → Removes what is on the top of the stack, and returns that value to the caller
    - top() → Looks at the top value, and returns it. Does not manipulate the stack
    - isEmpty() → Returns True or False if the stack is Empty or not, respectively
    - size() → Returns an integer value with the count of elements in the stack

Here is a sample execution trace:
myStack = Stack()
myStack.push(42)
print “Top of stack: ”, myStack.top()
# prints “Top of stack: 42”
print “Size of stack: ”, myStack.size()
# prints “Size of stack: 1”
popped_value = myStack.pop(42)
print “Popped value: ” , popped_value
# prints “Popped value: 42”
print “Size of stack: ”, myStack.size()
# prints “Size of stack: 0”

Make sure to write extension unit tests for your stack. Consider, for example, what would happen if you pop off more
items than you push.

Bonus: - if you want to push yourself further, try these extra challenges!
    - Add a new method to your Stack class called min(), which returns the minimum element of the stack in O(1) time, as
    opposed to O(n) time.
    - Allow your stack to handle any type of object as input type, not just integers.
"""
class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class Stack:
    def __init__(self):
        self.topNode = None
        # self.min = None
        self.size = 0

    def push(self, value):
        if not self.topNode:
            self.topNode = Node(value)
            # self.min = value
        else:
            self.topNode = Node(value, self.topNode)
            # if value < self.min:
            #     self.min = value
        self.size += 1

    def pop(self):
        if self.topNode == None: raise
        aux = self.topNode.value
        self.topNode = self.topNode.next
        self.size -= 1
        return aux

    def top(self):
        return self.topNode.value

    def isEmpty(self):
        return self.topNode == None

    def sizeN(self):
        counter = 0
        if self.topNode:
            aux = self.topNode
            while aux:
                counter +=1
                aux = aux.next
        return counter

    def size1(self):
        return self.size
    #
    # def min(self):
    #     if not self.topNode: raise
    #     return self.min


'''
Complexity analysis:
  push(): O(1)
  pop(): O(1) 
  top(): O(1) 
  isEmpty(): O(1) 
  sizeN(): O(n)
  size1(): O(1) 
  min(): O(1) 
'''


'''
Queue

A queue is a particular kind of abstract data type in which the entities in the collection are kept in order and 
the principle (or only) operations on the collection are the addition of entities to the rear terminal position, 
known as enqueue, and removal of entities from the front terminal position, known as dequeue. This makes the queue a 
First-In-First-Out (FIFO) data structure. 
			
Implement a Queue class from scratch that handles integers, with the following methods: 
    - enqueue() → adds an item to the queue
    - dequeue() → removes an item from the queue
    - rear() → returns the item at the end of the queue
    - front() → returns the item at the front of the queue
    - ize() → returns the size of the queue
    - isEmpty() → returns whether or not the queue is empty


Here is a sample execution trace:
myQueue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print “Size of queue: “, queue.size()
# prints “Size of queue: 3”
print “Front of queue: “, queue.front()
# prints “Front of queue: 1”
print “Rear of queue: “, queue.rear()
# prints “Rear of queue: 3”
dequeuedItem = queue.dequeue()
print “Dequeue item: “, dequeuedItem
# prints “Dequeued item: 1”

Make sure to write extension unit tests for your queue. Consider, for example, what would happen if you dequeue more 
items than you enqueue. 

Bonus 
    - Allow your queue to handle any type of object as input type, not just integers. 

'''

class Queue:
    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        newnode = Node(value)
        if self.last:
            self.last.next = newnode
            self.last = newnode
        else:
            self.top = self.last = newnode
        self.size += 1

    def dequeue(self):
        if not self.top: raise
        aux = self.top.value
        self.top = self.top.next
        self.size -= 1
        return aux

    def rear(self):
        if not self.last: raise
        return self.last.value

    def front(self):
        if not self.top: raise
        return self.top.value

    def sizeN(self):
        counter = 0
        aux = self.top
        while aux != None:
            counter += 1
            aux = aux.next
        return counter

    def size1(self):
        return self.size

    def isEmpty(self):
        return self.top == None


'''                 
Complexity analysis:
  enqueue(): O(1)      
  dequeue(): O(1)       
  rear(): O(1)       
  front(): O(1)   
  sizeN(): O(n)     
  size1(): O(1)     
  isEmpty(): O(1)       
'''


print("################ RUNNING TESTS ################")
print('\n1) Stack')
myStack = Stack()
myStack.push(42)
print("Top of stack:", myStack.top(), "(Expected: 42)")
print("Size of stack:", myStack.size1(), "(Expected: 1)")
print("Is stack empty:", myStack.isEmpty(),"(Expected: False)")
popped_value = myStack.pop()
print("Popped value:" , popped_value, " (Expected: 42)")
print("Size of stack:", myStack.size1()," (Expected: 0)")
print("Is stack empty:", myStack.isEmpty(),"(Expected: True)")
myStack.push(42)
myStack.push(1.324)   
myStack.push("carla")
print("Size of stack:", myStack.size1(),"(Expected: 3)")
print("Top of stack:", myStack.top(), "(Expected: carla)")

print('\n2) Queue')
myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print("Size of queue:", myQueue.size1(), "(Expected: 3)")
print("Front of queue:", myQueue.front(),"(Expected: 1)")
print("Rear of queue:", myQueue.rear(), "(Expected: 3)")
dequeuedItem = myQueue.dequeue()
print("Dequeue item: ", dequeuedItem, "(Expected: 1)")
print("Size of queue:", myQueue.size1(), "(Expected: 2)")
myQueue.enqueue("carla")
print("Rear of queue:", myQueue.rear(), "(Expected: carla)")
class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class Stack:
    def __init__(self):
        self.top_node = None
        self._min = None
        self.size = 0

    def push(self, value):
        if self.isEmpty():
            self.top_node = Node(value)
            self._min = value
        else:
            try:
                if value < self._min:
                     self._min = value
            except TypeError:
                print(f"Invalid input. Empty the stack first or add an object {type(self.top_node.value)}")
                return
            else:
                self.top_node = Node(value, self.top_node)
        self.size += 1

    def pop(self):
        if self.isEmpty(): raise Exception("Empty Stack")
        aux = self.top_node.value
        self.top_node = self.top_node.next
        self.size -= 1
        return aux

    def top(self):
        return self.top_node.value

    def isEmpty(self):
        return self.top_node == None

    def sizeN(self):
        counter = 0
        if self.top_node:
            aux = self.top_node
            while aux:
                counter +=1
                aux = aux.next
        return counter

    def size1(self):
        return self.size

    def min(self):
         if self.isEmpty(): raise Exception("Empty Stack")
         return self._min


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


class Queue:
    def __init__(self):
        self.top = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.last:
            self.last.next = new_node
            self.last = new_node
        else:
            self.top = self.last = new_node
        self.size += 1

    def dequeue(self):
        if self.isEmpty(): raise Exception("Empty Queue")
        aux = self.top.value
        self.top = self.top.next
        self.size -= 1
        return aux

    def rear(self):
        if self.isEmpty(): raise Exception("Empty Queue")
        return self.last.value

    def front(self):
        if self.isEmpty(): raise Exception("Empty Queue")
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
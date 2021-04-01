import sys

class NodeWithMin:
    def __init__(self, value, min):
        self.value = value
        self.min = min


class StackWithMin1:

    def __init__(self):
        self._stack = []

    def push(self, value):
        new_min = min(value, self.min())
        self._stack.append(NodeWithMin(value, new_min))

    def pop(self):
        return self._stack.pop()

    def min(self):
        if not self._stack: return sys.maxsize
        return self._stack[-1].min


class StackWithMin2:
    def __init__(self):
        self.stack = []
        self.stack_mins = []

    def push(self, value):
        if value <= self.min():
            self.stack_mins.append(value)
        self.stack.append(value)

    def pop(self):
        value = self.stack.pop()
        if value == self.min():
            self.stack_mins.pop()
        return value

    def min(self):
        if not self.stack: return sys.maxsize
        return self.stack_mins[-1]


stack1 = StackWithMin1()
stack1.push(5)
stack1.push(6)
stack1.push(3)
stack1.push(7)
print(stack1.min())
stack1.pop()
stack1.pop()
print(stack1.min())

stack2 = StackWithMin2()
stack2.push(5)
stack2.push(6)
stack2.push(3)
stack2.push(7)
print(stack2.min())
stack2.pop()
stack2.pop()
print(stack2.min())
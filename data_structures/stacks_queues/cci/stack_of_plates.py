class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, value):
        last_stack = self.stacks[-1]
        if last_stack and len(last_stack) > self.capacity:
            last_stack.append(value)
        else:
            new_stack = []
            new_stack.append(value)
            self.stacks.append(new_stack)

    def pop(self):
        last_stack = self.stacks[-1]
        value = last_stack.pop()
        if not last_stack:
            self.stacks.remove(last_stack)
        return value

    def popAt(self, index):
        stack = self.stacks[index]
        value = stack.pop()
        if not stack:
            self.stacks.remove(stack)
        return value
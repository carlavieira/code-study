class MyQueue:
    def __init__(self):
        self.newest_on_top = []
        self.oldest_on_top = []

    def add(self, value):
        self.newest_on_top.append(value)

    def peek(self):
        self.check_oldest()
        return self.oldest_on_top[-1]

    def remove(self):
        self.check_oldest()
        return self.oldest_on_top.pop()
        
    def check_oldest(self):
        if not self.oldest_on_top:
            while self.newest_on_top:
                self.oldest_on_top.append(self.newest_on_top.pop())

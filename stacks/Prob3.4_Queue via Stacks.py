class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, num):
        self.list.append(num)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()


class QueueViaStack():
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enterItemInQueue(self, num):
        self.inStack.push(num)

    def deQueue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        poppedElem = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())

        return poppedElem
    
customQueue = QueueViaStack()
customQueue.enterItemInQueue(1)
customQueue.enterItemInQueue(44)
customQueue.enterItemInQueue(93)
customQueue.enterItemInQueue(34)

print(customQueue.deQueue())


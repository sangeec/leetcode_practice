class SortedStack():
    def __init__(self) -> None:
        self.stack = []
        self.tempStack = []

    def pushItem(self, item):
        while self.stack and item > self.stack[-1]:
            self.tempStack.append(self.stack.pop())
        self.stack.append(item)
        while self.tempStack:
            self.stack.append(self.tempStack.pop())

    def popItem(self):
        if len(self.stack) == 0:
            return None
        else:
            poppedItem = self.stack.pop()
            return poppedItem
        
    def peekItem(self):
        if len(self.stack) == 0:
            return None
        else:
            peakElem = self.stack[-1]
            return peakElem
        
    def isEmpty(self):
        return len(self.stack) == 0
    
sorted_stack = SortedStack()
sorted_stack.pushItem(5)
sorted_stack.pushItem(2)
sorted_stack.pushItem(8)
sorted_stack.pushItem(1)   

while not sorted_stack.isEmpty():
    print(sorted_stack.popItem())
    # print("peak = ", sorted_stack.peekItem())
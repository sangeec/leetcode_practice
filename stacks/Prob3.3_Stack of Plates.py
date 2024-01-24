class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def __str__(self):
        return self.stack
    
    def push(self, num):
        if len(self.stack) > 0 and len(self.stack[-1]) < self.capacity:
            self.stack[-1].append(num)
        else:
            self.stack.append([num])

    def pop(self):
        while len(self.stack[-1]) or len(self.stack) == 0:
            self.stack.pop()
        if len(self.stack[-1]) or len(self.stack) == 0:
            return None
        else:
            return self.stack[-1].pop()
        
    def popAt(self, index):
        if len(self.stack[index]) > 0:
            return self.stack[index].pop()
        else:
            return None
        

customStack = PlateStack(2)
customStack.push(23)
customStack.push(29)
customStack.push(10)
customStack.push(53)
customStack.push(9)
# print("custom stack is ", customStack)
print(customStack.popAt(2))
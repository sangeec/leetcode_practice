class MinStack:
    def __init__(self):
        
        self.stack = []

    def push(self, value):
        
        if not self.stack or value < self.stack[-1][1]:
            self.stack.append((value, value))
        else:
            self.stack.append((value, self.stack[-1][1]))

    def pop(self):
        if not self.stack:
            return None
        
        return self.stack.pop()[0]

    def min(self):
        if not self.stack:
            return None
        return self.stack[-1][1]

# Example usage:
stack = MinStack()
stack.push(3)
stack.push(5)
print("Current minimum:", stack.min()) 
stack.push(2)
print("Current minimum:", stack.min()) 
stack.pop()
print("Current minimum:", stack.min()) 

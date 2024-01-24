class ThreeStack:
    def __init__(self, cap=2):
        cap *= 3
        self.items = [None]*cap
        self.start = [0, cap//3, 2*(cap//3)]
        self.end = [cap//3, 2*(cap//3), cap]

    def push(self, stack, val):
        if stack > 2:
            raise ValueError("stack {stack} does NOT exist")
        if self.start[stack] >= self.end[stack]:
            raise ValueError("stack {stack} is FULL!")
        self.items[self.start[stack]] = val
        self.start[stack] += 1

    def pop(self, stack):
        if stack > 2:
            raise ValueError("Stack {stack} does not exist")
        top = self.start[stack] - 1
        if top < 0 or self.items[top] == None:
            raise ValueError("stack {stack} is Empty")
        item = self.items[top]
        self.items[top] = None
        self.start[stack] = top
        return item

    def peek(self, stack):
        if stack > 2:
            raise ValueError("stack {stack} does not exist")
        top = self.start[stack] - 1
        if top < 0 or self.items[top] == None:
            raise ValueError("stack {stack} is empty")
        return self.items[top]

    def display(self):
        print(self.items)

a= ThreeStack()
a.push(1, 'C')
a.push(1, 'D')
# a.push(1, 'E')

a.display()

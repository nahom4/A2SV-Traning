class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or self.minStack and self.minStack[-1] > val:
            self.minStack.append(val)
        
    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.stack.pop()
            self.minStack.pop()
            for i in range(len(self.stack) - 1,-1,-1):
                if not self.minStack or self.stack[i] < self.minStack[-1]:
                    self.minStack.append(self.stack[i])
     
        else:
            self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
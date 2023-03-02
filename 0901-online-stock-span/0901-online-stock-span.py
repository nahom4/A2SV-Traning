class StockSpanner:

    def __init__(self):
        self.stack = []
        self.memory = []
        

    def next(self, price: int) -> int:
        #decreasing stack
        count = 1
        while self.stack and self.stack[-1] <= price:
            self.stack.pop()
            count += self.memory.pop()
        self.memory.append(count)
        self.stack.append(price)
        return self.memory[-1]
            
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
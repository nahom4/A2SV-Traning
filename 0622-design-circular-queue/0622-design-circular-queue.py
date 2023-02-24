class MyCircularQueue:

    def __init__(self, k: int):
        
        self.circular_queue = [None]*k
        self.size = 0
        self.capacity = k
        self.front = 0
        self.rear  = 0
        

    def enQueue(self, value: int) -> bool:
        #operation could be succesfull or not
        
        
        if self.circular_queue[(self.rear)] == None:
            self.circular_queue[(self.rear)] = value
            self.rear = (self.rear + 1)%self.capacity
            self.size += 1
            return True
            
        else:
            return False
        
        
        

    def deQueue(self) -> bool:
        if self.circular_queue[(self.front)%self.capacity] is not None:
            self.circular_queue[(self.front)%self.capacity] = None
            self.front = (self.front + 1)%self.capacity
            self.size -= 1
            return True
            
        else:
            return False
        

    def Front(self) -> int:
        if self.circular_queue[(self.front)%self.capacity] is not None:
            return self.circular_queue[self.front %self.capacity]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.circular_queue[(self.rear - 1)%self.capacity] is not None:
            return self.circular_queue[(self.rear - 1)]
        else:
            return -1
        

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        

    def isFull(self) -> bool:
        if self.size == self.capacity:
            return True
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
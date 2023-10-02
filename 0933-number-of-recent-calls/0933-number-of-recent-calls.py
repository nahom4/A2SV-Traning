class RecentCounter:

    def __init__(self):
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        self.queue.append(t)
        leftLimit = t - 3000
        while self.queue[0]  < leftLimit:
            self.queue.popleft()
        
        return len(self.queue)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
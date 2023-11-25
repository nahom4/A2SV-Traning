class AllOne:

    def __init__(self):
        self.ct  = Counter()
        self.minHeap = []
        self.maxHeap = []
        self.dateMap = defaultdict(int)

    def inc(self, key: str) -> None:
        self.ct[key] += 1
        self.dateMap[key] += 1
        heapq.heappush(self.minHeap,(self.ct[key],key,self.dateMap[key]))
        heapq.heappush(self.maxHeap,(-self.ct[key],key,self.dateMap[key]))
    def dec(self, key: str) -> None:
        self.ct[key] -= 1
        self.dateMap[key] += 1

        if self.ct[key] == 0:
            self.dateMap[key] += 1
            return
        heapq.heappush(self.minHeap,(self.ct[key],key,self.dateMap[key]))
        heapq.heappush(self.maxHeap,(-self.ct[key],key,self.dateMap[key]))


    def getMaxKey(self) -> str:

        while len(self.maxHeap) > 0:
            ct,string,date = heapq.heappop(self.maxHeap)
            if self.dateMap[string] == date:
                heapq.heappush(self.maxHeap,(ct,string,date))
                return string
        return ""

    def getMinKey(self) -> str:
        while len(self.minHeap) > 0:
            ct,string,date = heapq.heappop(self.minHeap)
            if self.dateMap[string] == date:
                heapq.heappush(self.minHeap,(ct,string,date))
                return string
        return ""
       

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
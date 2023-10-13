class LRUCache:

    def __init__(self, capacity: int):
        self.lruCache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
    
        if key in self.lruCache:
            
            val = self.lruCache[key]
            self.lruCache.pop(key)
            self.lruCache[key] = val
            return val
        
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.lruCache:
                self.lruCache.pop(key)
                
        elif len(self.lruCache) == self.capacity:
                lruKey = next(iter(self.lruCache.keys())) 
                self.lruCache.pop(lruKey)
                
        self.lruCache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
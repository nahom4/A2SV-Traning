class MyHashMap:

    def __init__(self):
        self.hashMap = [None] * (10 ** 6 + 1)

    def put(self, key: int, value: int) -> None:
        
        self.hashMap[key] = value

    def get(self, key: int):
        if  self.hashMap[key] == None:
            return -1
        return self.hashMap[key]

    def remove(self, key: int) -> None:
        self.hashMap[key] = None
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
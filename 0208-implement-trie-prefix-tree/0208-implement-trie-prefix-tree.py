class Trie:

    def __init__(self):
        self.children = [None for _ in range(27)]
        self.isEnd = False
        

    def insert(self, word: str) -> None:
        pool = self.children # [None,None]
        for letter in word:
            idx = ord(letter) - 96
            if not pool[idx]:
                pool[idx] = Trie()  # self.children = [None,None] self.isEnd = False
                
            node = pool[idx]
            pool = node.children
        node.isEnd = True
    def search(self, word: str) -> bool:
        pool = self.children
        for letter in word:
            idx = ord(letter) - 96
            if not pool[idx]:
                return False
            node = pool[idx]
            pool = node.children
            
        return node.isEnd
   
    def startsWith(self, prefix: str) -> bool:
        pool = self.children
        for letter in prefix:
            idx = ord(letter) - 96
            if not pool[idx]:
                return False
            
            pool = pool[idx].children
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
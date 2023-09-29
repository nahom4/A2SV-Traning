class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.value = 0
        self.letter = "*"
        
    def addWord(self,word,value):
        pool = self.children
        N = len(word)
        for letter in word:
            if not letter in pool:
                pool[letter] = Trie()
            node = pool[letter]
            node.letter = letter
            pool = node.children
            
        node.isEnd = True
        node.value = value
        
        
class MapSum:

    def __init__(self):
        self.trie = Trie()
 
    def insert(self, key: str, val: int) -> None:
        self.trie.addWord(key,val)
        
    def locateStartNode(self,prefix,node): # a {} pre p
        if not prefix:
            return node
        pool = node.children # pool {}
        if not prefix[0] in pool:
            return None
        return self.locateStartNode(prefix[1:],pool[prefix[0]])
    
    def sum(self, prefix: str) -> int:
    
        start = self.locateStartNode(prefix,self.trie)
        def dfs(node):
            if not node:
                return 0
            pool = node.children
            count = 0
            for child in pool:
                count += dfs(pool[child])  
                
            count += node.value
            return count
                
        return dfs(start)
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
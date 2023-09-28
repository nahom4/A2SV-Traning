class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self,word):
        pool = self.children
        N = len(word)
        for letter in word:
            if not letter in pool:
                pool[letter] = Trie()
            node = pool[letter] 
            pool = node.children
            
        node.isEnd = True
                
class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.addWord(word)
    
    def search(self, word: str) -> bool:
        def findWord(node,word):
            if not word:
                if node.isEnd:
                    return True
                else:
                    return False
            
            res = False
            pool = node.children
            if word[0] in pool:
                res = res or findWord(pool[word[0]],word[1:]) 
            if word[0] == ".":
                for value in pool:
                    res = res or findWord(pool[value],word[1:])
                    
            return res
        return findWord(self.trie,word)
            
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
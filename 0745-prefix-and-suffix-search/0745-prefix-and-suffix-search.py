class Trie:
    def __init__(self):
        self.children = {}
        self.weight = None
        self.value = None
        
    def addWord(self,word,index):
        N = len(word)
        pool = self.children
        for i in range(N):
            if not word[i] in pool:
                pool[word[i]] = Trie()
               
            node = pool[word[i]]
            node.weight = index
            pool = node.children
            
    def findWord(self,word):
        pool = self.children
        N = len(word)
        for i in range(N):
            if not word[i] in pool:
                return -1
            node = pool[word[i]]
            pool = node.children
            
        return node.weight
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for index, word in enumerate(words):
            N = len(word)
            for i in range(N,-1,-1):
                newWord = word[i : ] + "{" + word
                self.trie.addWord(newWord,index)
    
    def f(self, pref: str, suff: str) -> int:
        return self.trie.findWord(suff + "{" + pref)
        
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
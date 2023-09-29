class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self,word):
        N = len(word)
        node = self
        pool = node.children
        for i in range(N):
            if not word[i] in pool:
                pool[word[i]] = Trie()
                
            node = pool[word[i]]
            pool = node.children
            
        node.isEnd = True
        
    def findWord(self,word):
        if not word:
            return True
        N = len(word)
        node = self
        pool = node.children
        for i in range(N):
            if not word[i] in pool:
                return False
            node = pool[word[i]]
            pool = node.children
            
        return node.isEnd
            
                      
class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words = sorted(words,key = lambda word : len(word))
        ans = ""
        trie = Trie()
        for word in words:
            if trie.findWord(word[:-1]):
                trie.addWord(word)
                if len(word) > len(ans):
                    ans = word
                elif len(word) == len(ans) and word < ans:
                    ans = word
        return ans
        
        
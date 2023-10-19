class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        
    def addWord(self,word):
        N = len(word)
        pool = self.children
        for i in range(N):
            if not word[i] in pool:
                pool[word[i]] = Trie()
                
            node = pool[word[i]]
            pool = node.children
            
        node.isEnd = True
        
    def findWord(self,word):
        N = len(word)
        node = self
        pool = self.children
        for i in range(N):
            if not word[i] in pool:
                return False
                
            node = pool[word[i]]
            pool = node.children

        return node.isEnd

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        wordSet = set(words)
        @cache
        def dp(word):
            if word == "":
                return 0
            
            N = len(word)
            valid = False
            count = float("-inf")
            for i in range(N):
                prevCount = float("-inf")
                sub = word[ : i + 1]

                if trie.findWord(sub):
                    prevCount = dp(word[i + 1 :]) + 1

                count = max(count,prevCount)
               
            return count 
        ans = []
        
        for word in words:
            trie.addWord(word)
          
        for word in words:
            if dp(word) > 1:
                ans.append(word)
           
        return ans
                
            
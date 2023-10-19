class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.count = 0
        
    def addWord(self,word):
        N = len(word)
        pool = self.children
        for i in range(N):
            if not word[i] in pool:
                pool[word[i]] = Trie()
                
            node = pool[word[i]]
            node.count += 1
            pool = node.children
            
        node.isEnd = True
        
        
                
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.addWord(word)
         
        ans = []
        for word in words:
            ct = 0
            node = trie
            for char in word:
                node = node.children[char]
                ct += node.count
                    
            ans.append(ct)
            
        return ans
                
            
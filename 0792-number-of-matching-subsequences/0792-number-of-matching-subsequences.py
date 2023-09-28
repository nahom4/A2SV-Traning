class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.isSeen = False
        self.count = 0
        self.value = None
        
    def addWord(self,word):
        node = self
        N = len(word)
        pool = node.children
        for i in range(N):
            if not word[i] in pool:
                pool[word[i]] = Trie()
            
            node = pool[word[i]]
            node.value = word[i]
            pool = node.children
            
        node.isEnd = True
        node.count += 1
        
            
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.addWord(word)
            
        def recursion(i,node):
    
            N = len(s)
            pool = node.children
            count = 0
            for child in pool: # "a" child pool {"a","b"}
                for j in range(i,N):
                    if s[j] == child: # I cut here "abcde" "bcde" node a  "cde" node b
                        count += recursion(j + 1,pool[s[j]])
                        break
               
            if node.isEnd:
                count += node.count
  
            return count
        
        return recursion(0,trie)
                    
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.value = None
        self.count = 0
        
    def addWord(self,word):
        N = len(word)
        pool = self.children
        for i in range(N):
            idx = ord(word[i]) - 97
            if not pool[idx]:
                pool[idx] = Trie()
                pool[idx].value = word[i]
                
            node = pool[idx]
            node.count += 1
            pool = node.children
            
        node.isEnd = True
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        for word in words:
            trie.addWord(word)
            
        ans = []
        for word in words: #1000
            N = len(word)
            count = 0
            pool = trie.children
            for j in range(N):
                char = word[j]
                idx = ord(char) - 97
                if not pool[idx]:
                    return None
                node = pool[idx]
                count += node.count
                pool = node.children

            ans.append(count)
        return ans
                
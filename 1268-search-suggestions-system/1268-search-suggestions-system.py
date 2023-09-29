class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.value = None
        
    def addWord(self,word):
        N = len(word)
        pool = self.children
        for i in range(N):
            idx = ord(word[i]) - 97
            if not pool[idx]:
                pool[idx] = Trie()
                pool[idx].value = word[i]
                
            node = pool[idx]
            pool = node.children
            
        node.isEnd = True
        
    def getStart(self,prefix):
        pool = self.children
        N = len(prefix)
        for i in range(N):
            char = prefix[i]
            idx = ord(char) - 97
            if not pool[idx]:
                return None
            node = pool[idx]
            pool = node.children
            
        return node
        
    def getThreeProducts(self,prefix):
        
        start = self.getStart(prefix)
        if start == None:
            return []
     
        def dfs(node,ans,curr):
    
            if len(ans) >= 3:
                return ans
            
            if node.isEnd:
                newWord = prefix + "".join(curr)
                ans.append(newWord)
              
            pool = node.children
           
            for i in range(26):
                if not pool[i]:
                    continue
                    
                char = chr(i + 97)
                curr.append(char)
                res = dfs(pool[i],ans,curr)
                curr.pop()
                    
            return ans
        return dfs(start,[],[])
                
class Solution(object):
    def __init__(self):
        self.trie = Trie()
        
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        for product in products:
            self.trie.addWord(product)
            
        N = len(searchWord)
        ans = []
        for i in range(N):
            ans.append(self.trie.getThreeProducts(searchWord[: i + 1]))
        
        return ans
            
        
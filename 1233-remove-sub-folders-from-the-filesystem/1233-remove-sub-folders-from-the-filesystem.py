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
        
        
    def collectFolders(self):
        ans = []
        def dfs(node,seen,words):
            
            currStatus = node.isEnd or seen
            pool = node.children
            for char in pool:
                words.append(char)
                dfs(pool[char],currStatus,words)
                words.pop()
                
            if not seen and node.isEnd:
                ans.append("/".join(words))
                
        dfs(self,False,[])
        return ans
                
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.addWord(f.split("/"))
            
        return trie.collectFolders()
        
        
        
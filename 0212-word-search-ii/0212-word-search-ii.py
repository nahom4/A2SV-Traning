class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def createTrie(self,word):
            curr = self
            for c in word:
                if not c in curr.children:
                    curr.children[c] = Trie()
                curr = curr.children[c]
            curr.isWord = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        N,M = len(board),len(board[0])
                     
        for word in words:
            root.createTrie(word)
            
        res,visited = set(),set() 
       
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(pos,node,word):
            row,col = pos
           
            if not (0 <= row < N and 0 <= col < M):
                return
            boardLetter = board[row][col]
            if not boardLetter in node.children or pos in visited:
                return
            
            word += boardLetter
            node = node.children[boardLetter]
            visited.add(pos)
            if node.isWord:
                res.add(word)   
            for x,y in direction:
                dfs((row + x,col + y),node,word)
            visited.remove(pos)
            
        for i in range(N):
            for j in range(M):
                
                dfs((i,j),root,"")
                
        return res
            
        
       
                
       
                    
            
                
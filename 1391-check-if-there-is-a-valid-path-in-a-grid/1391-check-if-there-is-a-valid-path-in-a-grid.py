class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        
        sides = {1 : ["left","right"], 2: ["top","bottom"],3 : ["left","bottom"],4: ["bottom","right"],5: ["top","left"], 6: ["top","right"]}
        mapping = {(0,1) : "right",(0,-1) : "left",(1,0) : "bottom",(-1,0) : "top"}
        rep = {(i,j) : (i,j) for i in range(n) for j in range(m)}
        size = {(i,j) : 1 for i in range(n) for j in range(m)}
        compliment = {"top" : "bottom","right": "left","bottom" : "top","left" : "right"}
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def valid_path(first,second,orientation):
            direc = mapping[orientation]
            row1,col1 = first
            row2,col2 = second
            road1 = grid[row1][col1]
            road2 = grid[row2][col2]
            
            return direc in sides[road1] and compliment[direc] in sides[road2]
           
        def is_valid(pos):
            row,col = pos
            
            return 0 <= row < n and 0 <= col < m
        
        def find(node):
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(first,second,orientation):
            
            firstParent = find(first)
            secondParent = find(second)
            
            if valid_path(first,second,orientation):
                
                if firstParent == secondParent:
                    return
                
                if size[firstParent] < size[secondParent]:
                    firstParent,secondParent = secondParent,firstParent
                  
                size[firstParent] += size[secondParent]
                rep[secondParent] = firstParent
                
                  
        for row in range(n):
            for col in range(m):
                
                for x,y in direction:
                    if is_valid((row + x,col + y)):
                        union((row,col),(row + x, col + y),(x,y))
                
            
                    
        return rep[(0,0)] == rep[(n - 1,m - 1)]
        
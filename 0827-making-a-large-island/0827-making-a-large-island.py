class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        N,M = len(grid),len(grid[0])
        rep = {(i,j) : (i,j) for i in range(N) for j in range(M)}
        rank ={(i,j) : grid[i][j] for i in range(N) for j in range(M)}
        maxSize = 0
        def find(node):
            
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        
        def union(firstNode,secondNode):
            nonlocal maxSize
            firstNodeParent,secondNodeParent = find(firstNode),find(secondNode)
            
            if firstNodeParent == secondNodeParent:
                return 
                   
            if rank[firstNodeParent] < rank[secondNodeParent]:
                firstNodeParent,secondNodeParent = secondNodeParent,firstNodeParent
            rep[secondNodeParent] = firstNodeParent
            rank[firstNodeParent] += rank[secondNodeParent]
            maxSize = max(maxSize,rank[firstNodeParent])
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    for x,y in direction:
                        if 0 <= (x + i) < N and  0 <= (y + j) < M:
                            if grid[x + i][j + y] == 1:
                                union((i,j),(x + i,y + j))
               
        for i in range(N):
            for j in range(M):
                currSize = 1
                seen = set()
                if grid[i][j] == 0:
                    for x,y in direction:
                        nxtR,nxtC = x + i,y + j
                        if 0 <= nxtR < N and  0 <= nxtC < M:
                             if grid[nxtR][nxtC] == 1:
                                    parent = find((nxtR,nxtC))
                                    if not parent in seen:
                                        currSize += rank[parent]
                                        seen.add(parent)
                maxSize = max(maxSize,currSize)
                                    
        return maxSize
        
                    
            
            
                
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        #let's try brut force approach
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        N = len(grid)
        M = len(grid[0])
        
        
        numOpenSqueres = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    start = (i,j)
                    
                if grid[i][j] == 2:
                    target = (i,j)
                    
                if grid[i][j] == 0:
                    numOpenSqueres += 1
         
        def noObstacle(pos):
            row,col = pos
            return grid[row][col] != -1
        def inBound(pos):
            row,col = pos
            
            return 0 <= row < N and 0 <= col < M
                
        def dp(start,path):
            
            row,col = start
            if len(path) == (numOpenSqueres + 2) and start == target:
                return 1
            
            count = 0
            for x,y in direction:
                nxtCoord = (row + x,col + y)
                if not nxtCoord in path and inBound(nxtCoord) and noObstacle(nxtCoord) :
                    path.add(nxtCoord)
                    count += dp(nxtCoord,path)
                    path.remove(nxtCoord)
                
            return count
        st = set()
        st.add(start)
        return dp(start,st)
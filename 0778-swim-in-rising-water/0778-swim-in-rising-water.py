class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #what are the variables we have t  and the diff's
        N = len(grid)
        M = len(grid[0])
        def inBound(row,col):
            return 0 <= row < N and 0 <= col < M
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        target = (N - 1, M - 1)
        fringe = [(0,0,0)]
        visited = set()
        while fringe:
            time,row,col = heapq.heappop(fringe)
            if target == (row,col):
                return time
            if (row,col) in visited:
                continue
                                         
            visited.add((row,col))
            for x,y in direction:
                nxtRow,nxtCol = row + x,col + y
                if inBound(nxtRow,nxtCol):
                    height = max(grid[nxtRow][nxtCol],grid[row][col])
                    currHeight = grid[row][col]
                    diff = abs(currHeight - height)
                    if height > time:
                        heapq.heappush(fringe,(height,nxtRow,nxtCol))
                        
                    else:
                        heapq.heappush(fringe,(time,nxtRow,nxtCol))
                    
                    
                        
                        
                        
                    
            
        
        
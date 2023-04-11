class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        result = 0
        def valid(pos):
            row,col = pos
            
            return 0 <= row and row  < len(grid) and 0 <= col and col < len(grid[0]) and grid[row][col] == 1
        
        def dfs(pos):
            
            direction = [(1,0),(-1,0),(0,1),(0,-1)]
            count = 1
            row,col = pos
            grid[row][col] = 0
            #go in the four directions
            for drc in direction:
                new_pos = ((pos[0] + drc[0]),(pos[1] + drc[1]))
                if valid(new_pos):
                    count += dfs(new_pos)
                
            return count
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    result = max(dfs((i,j)), result)
                    
                    
        return result
        
        
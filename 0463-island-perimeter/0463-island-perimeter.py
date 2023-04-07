class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
   
        # let's do dfs
        visited = set()
        perimetere = 0
        
        def in_bound(index):
            row,col = index
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
            
            return index > 0
        
        def dfs(index):
           
            nonlocal perimetere
           
        
            if index in visited:
                return
            
            visited.add(index)
            #calculate perimetere we do this only if we are out bounds
            # or we get to a water
            row,col = index
            if grid[row][col] == 1:
                
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimetere += 1

                if row + 1 >= len(grid) or grid[row + 1][col] == 0:
                    perimetere += 1
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimetere += 1

                if col + 1 >= len(grid[0]) or grid[row][col + 1] == 0:

                    perimetere += 1
            
           
            # go in the four directions
            
            #up
            if in_bound((row - 1,col)):
                dfs((row - 1,col))
            #down
            if in_bound((row + 1,col)):
                dfs((row + 1,col))
                
            #right
            if in_bound((row,col + 1)):
                dfs((row,col + 1))
            #left 
            if in_bound((row, col - 1)):
                dfs((row,col - 1))
            
        dfs((0,0))    
        return perimetere
        
        
        
        
        
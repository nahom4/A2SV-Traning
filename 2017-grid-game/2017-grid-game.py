import math
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        #calculate prefix sum
        for row in range(2):
            for col in range(1,n):
                grid[row][col] += grid[row][col - 1]
       
        result = math.inf  
        for col in range(n):
            #There are different possible turns
          
            if col == 0:
                temp = grid[0][n - 1] - grid[0][0]
               
                
            elif col == n - 1:
                temp = grid[1][n - 2]
               
                
            else:
                temp = max(grid[1][col - 1], grid[0][n - 1] - grid[0][col])
                
            result = min(result,temp)
        
        return result
                
                
            
        
        
        




    
       
      
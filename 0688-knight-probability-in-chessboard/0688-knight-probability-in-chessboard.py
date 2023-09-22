class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # let's do this top down
        
        direction = [(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        def inBound(row,col):
            return 0 <= row < n and 0 <= col < n
        
        cache = {}
        def dp(row,col,k):
            
            if not inBound(row,col):
                return 0
            
            if k <= 0:
                return 1
            
            if (row,col,k) in cache:
                return cache[(row,col,k)]
            
            count = 0
            for x,y in direction:
                count += dp(row + x,col + y,k - 1)
             
            cache[(row,col,k)] = count
            return count 
        
        res = dp(row,column,k)
        return (res) / 8 ** k
                    
                
                    
            
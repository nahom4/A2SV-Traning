class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        N = len(matrix)
        M = len(matrix[0])
        direction = [(1,0),(1,-1),(1,1)]
        cache = {}
        def inBound(row,col):
            return 0 <= row < N and 0 <= col < M
        
        def dp(row,col):
              
            if row == N - 1:
                return matrix[row][col]
                
            if (row,col) in cache:
                return cache[(row,col)]
              
            fallindDistance = float("inf")
            for x,y in direction:
                
                if not inBound(row + x,col + y):
                    continue
                  
                fallindDistance = min(fallindDistance,dp(row + x,col + y))
        
            cache[(row,col)] = fallindDistance + matrix[row][col]
            return cache[(row,col)]
        
        ans = float("inf")
        for i in range(N):
            ans = min(dp(0,i),ans)
            
        return ans
        
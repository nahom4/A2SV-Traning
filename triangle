class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        cache = {}
        
        def minTriangle(pos):
            row,col = pos
            
            #base case when I reach the bottom
            if row == len(triangle) - 1:
                return triangle[row][col]
            
            if not pos in cache:
                first = minTriangle((row + 1,col))
                second = minTriangle((row + 1, col + 1))
                cache[pos] = triangle[row][col] + min(first,second)
             
            return cache[pos]

        return minTriangle((0,0))
        
        
        
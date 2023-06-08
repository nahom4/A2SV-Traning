class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def uniquePath(pos,target):
            row,col = pos
            if row >= target[0] or col >= target[1]:
                return 0
            #base case
            if row == target[0] - 1 and col == target[1] - 1:
                return 1 #count 1
            
            bottom = uniquePath((row + 1,col),target)
            right = uniquePath((row,col + 1),target)
            
            #return the sum of bottom and down
            return bottom + right
            
        return uniquePath((0,0),(m,n))    
            
        
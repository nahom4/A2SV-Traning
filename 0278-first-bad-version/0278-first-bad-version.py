# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        low = 0
        high = n + 1
        
        while high > low + 1:
            
            md = low + (high - low ) // 2
            if isBadVersion(md):
                high = md
            else:
                low = md
                
        return high
        
class Solution:
    def mySqrt(self, x: int) -> int:
        
        low = -1 
        high = x + 1
        
        while high > low + 1:
            
            md = low + (high - low)//2
          
            if md ** 2 <= x:
                low = md
            else:
                high = md
                
        return low
        
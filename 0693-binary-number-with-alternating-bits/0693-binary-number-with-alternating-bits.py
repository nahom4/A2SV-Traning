class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        flag = True
        prev = n & 1
        while n > 0:
            
            n = n >> 1
            curr = n & 1
            
            if curr == prev:
                flag = False
                break
            prev = curr
        
        return flag
            
            
        
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        Mod = 10 ** 9 + 7
        @cache
        def dp(i,steps):
            if steps <= 0:
                if i == 0:
                    return 1
                else:
                    return 0
                
            if i < 0 or i >= arrLen:
                return  0
            
            
            #stay 
            stay = dp(i,steps - 1)
            #left
            left = dp(i - 1, steps - 1)
            #right
            right = dp(i + 1,steps - 1)
            
            return (stay + left + right)
        
        
        return dp(0,steps) % Mod
            
            
                
        
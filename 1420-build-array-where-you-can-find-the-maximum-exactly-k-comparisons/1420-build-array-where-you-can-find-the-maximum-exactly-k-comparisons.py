class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        Mod = 10 ** 9 + 7
        @cache
        def dp(N,mx,k):
            
            if N == 0:
                if k == 0:
                    return 1
                
                return 0
            
            ct = 0
            for x in range(1,mx + 1):
                ct += dp(N - 1,mx,k)
                
            if k > 0:
                for x in range(mx + 1,m + 1):
                    ct += dp(N - 1,x,k - 1)
                
            return ct % Mod
            
            
        return dp(n,0,k) % Mod
        
       
                            
                    
                
                
        
        
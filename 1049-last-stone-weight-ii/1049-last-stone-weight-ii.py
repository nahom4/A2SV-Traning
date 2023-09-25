class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        N = len(stones)
        @cache
        def dp(sm,i):
            
            if i >= N:
                return abs(sm)
            
            ans = min(dp(sm + stones[i], i + 1), dp(sm - stones[i],i + 1))
            return ans
        
        return dp(0,0)
        
     
        
        
        
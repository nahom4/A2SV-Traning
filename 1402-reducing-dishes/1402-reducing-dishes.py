class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        """
            pick or don't pick
        """
        satisfaction.sort()
        N = len(satisfaction)
        @cache
        def dp(size,i):
            
            if i == N - 1:
                if satisfaction[i] > 0:
                    return size * satisfaction[i]
                
                else:
                    return 0
               
            pick = size * satisfaction[i] + dp(size + 1 , i + 1)
            leave = dp(size,i + 1)
            
            return max(pick,leave)
            
        return dp(1,0)
            
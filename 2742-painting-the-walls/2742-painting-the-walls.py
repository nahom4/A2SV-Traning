class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # @cache
        newTime = list(time)
        N = len(cost)
        totalTime = sum(time)          
        cache = {}
        def dp(i,remain):
            N = len(cost)
            
            if (i,remain) in cache:
                return cache[(i,remain)]
            
            if remain <= 0:
                return 0
            if i >= N:
                if remain > 0:
                    return float("inf")
                else:
                    return 0
                        
            paid = cost[i] + dp(i + 1,remain - 1 - time[i])
            free = dp(i + 1,remain)
            
            cache[(i,remain)] = min(paid,free)
            return min(paid,free)
        
        return dp(0,len(cost))
             
        
#         N = len(cost)
#         for i in range(N):
            
        
        
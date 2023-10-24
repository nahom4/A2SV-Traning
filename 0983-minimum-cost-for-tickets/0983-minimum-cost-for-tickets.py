class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        N = len(days)
        cache = defaultdict(int)
        for i in range(N - 1,-1,-1):
            day = cache[bisect.bisect_left(days,days[i] + 1)] + costs[0]
            week = cache[bisect.bisect_left(days,days[i] + 7)] + costs[1]
            month = cache[bisect.bisect_left(days,days[i] + 30)] + costs[2]
            
            cache[i] = min(day,week,month)
         
        return cache[0]
        # @cache
#         def dp(i):
            
#             if i >= len(days):
#                 return 0
#             #pay daily
#             day = dp(i + 1) + costs[0]
#             #pay weakly
#             week = dp(bisect.bisect_left(days,days[i] + 7)) + costs[1]
#             #pay monthy
#             month = dp(bisect.bisect_left(days,days[i] + 30)) + costs[2]
            
#             return min(day,week,month)
          
#         return dp(0)
    
        
    
        
        
        
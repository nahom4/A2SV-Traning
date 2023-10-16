class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(i):
            
            if i >= len(days):
                return 0
            #pay daily
            day = dp(i + 1) + costs[0]
            #pay weakly
            week = dp(bisect.bisect_left(days,days[i] + 7)) + costs[1]
            #pay monthy
            month = dp(bisect.bisect_left(days,days[i] + 30)) + costs[2]
            
            return min(day,week,month)
          
        return dp(0)
        
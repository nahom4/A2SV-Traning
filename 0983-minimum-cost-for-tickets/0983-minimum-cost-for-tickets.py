class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        cache = Counter()
        left = 0
        for i in range(1,max(days) + 1):
            if days[left] == i:
                left += 1
                day = cache[i - 1] + costs[0]
                week = cache[i - 7] + costs[1]
                month = cache[i - 30] + costs[2]
                cache[i] = min(day,week,month)
                
            else:
                cache[i] = cache[i - 1]
                
        return cache[max(days)]
            
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
    
        
    
        
        
        
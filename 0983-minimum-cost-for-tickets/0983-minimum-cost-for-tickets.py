class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
       
        @cache
        def dfs(i):
            
            N = len(days)
            if i >= N:
                return 0
            
            minCost = float("inf")
            for d,c in zip([1,7,30],costs):
                j = i
                while j < N and days[j] < days[i] + d:
                    j += 1
                  
                minCost = min(minCost,dfs(j) + c)
                
            return minCost
        return dfs(0)
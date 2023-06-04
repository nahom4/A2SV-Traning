class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        min_cost = float('inf')
       
        @cache
        def minCost(n):
            
            if n  >= len(cost):
                return 0
            
            oneStep = minCost(n + 1)
            twoStep = minCost(n + 2)
            
           
            
            return cost[n] + min(oneStep,twoStep)
        
        return min(minCost(0),minCost(1))
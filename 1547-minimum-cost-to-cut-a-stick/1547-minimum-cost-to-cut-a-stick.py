class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        @cache
        def dp(i,j):
                
            minCost = float("inf")
            for cut in cuts:
                if i < cut < j:
                    minCost = min(minCost,dp(i,cut) + dp(cut,j) + (j - i))
                     
            return minCost if minCost != float("inf") else 0
        
        return dp(0,n)
                    
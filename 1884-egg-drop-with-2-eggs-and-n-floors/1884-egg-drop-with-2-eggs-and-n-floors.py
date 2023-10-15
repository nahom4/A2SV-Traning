class Solution:
    def twoEggDrop(self, n: int) -> int:
        
        @cache
        def dp(numFloors,eggs):
            
            if numFloors == 1 or numFloors == 0 or eggs == 1:
                return numFloors
            
            minMove = float("inf")
            for i in range(1,numFloors):
                minMove = min(minMove ,max(dp(i - 1,eggs - 1) , dp(numFloors - i,eggs)))
                
            return minMove + 1
        
        return dp(n,2)
            
        
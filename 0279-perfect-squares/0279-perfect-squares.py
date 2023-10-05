class Solution:
    def numSquares(self, n: int) -> int:
        """
            [1,2,3,4] 
        """
        
        array = []
        for num in range(1,n + 1):
            root  = int(num ** 0.5)
            if root ** 2 == num:
                array.append(num)
           
        @cache
        def dp(sm): #[1,4,9]
            if sm > n:
                return float("inf")
            
            if sm == n:
                return 0
            minValue = float("inf")
            for value in array:
                minValue = min(dp(value + sm),minValue)
                
            return minValue + 1
        
        return dp(0)
                
      
        
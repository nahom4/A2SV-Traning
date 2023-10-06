class Solution:
    def integerBreak(self, n: int) -> int:
        #dp [1,2,3,4,5,6,7,8,9] >= 2 target 10
        
        if n == 2:
            return 1
        
        if n == 3:
            return 2
        @cache
        def dp(n):
            if n <= 3:
                return n
            
            if n <= 1:
                return 1
            
            #how can we devide n 1 2 3  4 5 6  N = 7
            maxProduct = 1
            for sub in range(1,n):
                firstHalve = sub # 1
                secondHalve = n - sub  # 3
                firstHalve = dp(firstHalve) # 1
                secondHalve = dp(secondHalve)
                maxProduct = max(maxProduct,firstHalve * secondHalve)
            
            return maxProduct
        return dp(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        lis = [-1] * 2*n
        def climbStairs(n):
            print(n)
            print(lis)
            if lis[n - 1] != -1:
                return lis[n - 1]
            if n < 0:
                return 0
            
            if n == 0:
                return 1
            
            lis[n - 1] = climbStairs(n - 1) + climbStairs(n - 2)
            
            return lis[n - 1]
        
        return climbStairs(n)
      
    
        
class Solution:
    def minSteps(self, n: int) -> int:
        d = 2
        result = 0
        while d * d <= n:
            print()
            if n % d == 0:
                result += d
                n = n // d
            else:
                d += 1
        if n != 1:
            result += n
                
        return result
            
            
   
        
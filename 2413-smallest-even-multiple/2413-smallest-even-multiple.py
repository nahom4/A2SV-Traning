class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        
        if n == 1:
            return 2
        if n%2 == 0:
            return n
        else:
            return n*2
        
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1: return 0
        prev = self.kthGrammar(n - 1,ceil(k/2))
        even = k % 2 == 0
        
        if prev == 1:
            return 0 if even else 1
        else:
            return 1 if even else 0
        
    
    
        
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        
        start = 0
        
        size = len(t)
        
        for i in range(size):
            
            if start < len(s) and t[i] == s[start]:
                start += 1
        if start < len(s):
            return False
        else:
            return True
                
                
        
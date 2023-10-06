class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            "aabcc"
            "dbbca"
            "aadbbcbcac"
        """
        @cache
        def dp(i,j):
            
            a = len(s1)
            b = len(s2)
            c = len(s3)
            
            if i >= a and j >= b and (i + j ) >= c:
                return True
            
            if (i + j) >= c:
                return False
            
            if i >= a and j >= b:
                return False
            
            top = bottom = False
            if i < a and s1[i] == s3[i + j]:
                top = dp(i + 1,j)
                
            if j < b and s2[j] == s3[i + j]:
                bottom = dp(i, j + 1)
                
        
            return top or bottom
        
        return dp(0,0)
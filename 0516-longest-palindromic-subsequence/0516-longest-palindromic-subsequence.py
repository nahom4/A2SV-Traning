class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        @cache
        def dp(left,right):
           
            if left == right:
                return 1
            
            if left > right:
                return 0
            
        
            if s[left] == s[right]:
                res = dp(left + 1,right - 1) + 2
                
            else:
                leftSide = dp(left + 1,right)
                rightSide = dp(left,right - 1)
                res = max(leftSide,rightSide)
                
                                   
            return res
        
        return dp(0,len(s) - 1)
        
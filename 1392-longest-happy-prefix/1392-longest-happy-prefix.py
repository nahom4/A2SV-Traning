class Solution:
    def longestPrefix(self, s: str) -> str:
        
        N = len(s)
        lps = [0] * N
        i,j = 1,0
        while i < N:
            
            if s[i] == s[j]:
                lps[i] = j + 1
                i += 1
                j += 1
                
            elif j == 0:
                i += 1
                
            else:
                j = lps[j - 1]
                
        return s[:lps[-1]]
        
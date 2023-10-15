class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        N = len(text1)
        M = len(text2)
        @cache
        def dp(i,j):
            if i >= N or j >= M:
                return 0
            
            
            if text1[i] == text2[j]:
                return dp(i + 1,j + 1) + 1
            
            else:
                return max(dp(i,j + 1),dp(i + 1,j))
            
        return dp(0,0)
        
#         N = len(text1) + 1 #abcde
#         M = len(text2) + 1 #ace
        
#         cache = [[0] * N for _ in range(M)]
        
        
#         for i in range(1,M):
#             for j in range(1,N):
                
#                 if text1[j - 1] == text2[i - 1]:
#                     cache[i][j] = 1 + cache[i - 1][j - 1]
                    
#                 else:
#                     cache[i][j] = max(cache[i - 1][j],cache[i][j - 1])
                    
#         return cache[M - 1][N - 1]
            
        
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        M = len(nums2)
        cache = [[float("-inf")] * (N + 1)  for _ in range((M + 1))]
        
        for i in range(N + 1):
            cache[0][i] = float("-inf")
            
        for i in range(M + 1):
            cache[i][0] = float("-inf")
            
        
        for i in range(1,M + 1):
            for j in range(1,N + 1):
                currProd = nums1[j - 1] * nums2[i - 1]
                prevValue = cache[i - 1][j - 1]
                if prevValue > 0:
                    currProd += prevValue
                    
                cache[i][j] = max(currProd,cache[i - 1][j],cache[i][j - 1])
                
        return cache[M][N]
                
        
        
        
#         if len(nums2) < len(nums1):
#             nums2,nums1 = nums1,nums2            
#         @cache
#         def dp(i,j):
            
#             #iterate over nums1
#             N = len(nums1)
#             M = len(nums2)
#             if i >= N:
#                 return float("-inf")
            
#             if j >= M:
#                 return float("-inf")
            
#             curr = dp(i + 1,j)
            
#             for k in range(j,M):
#                 res = dp(i + 1,k + 1)
#                 currProd = nums1[i] * nums2[k]
#                 if res < 0:
#                     currProd = max(currProd,res)
                    
#                 else:
#                     currProd += res
                    
#                 curr = max(curr,currProd)
                
#             return curr
        
#         return dp(0,0)
                
        
        
            
        
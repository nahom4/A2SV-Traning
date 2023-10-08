class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        target = total
        N = len(nums)
#         @cache
#         def dp(i,sm):
#             if i >= N:
#                 if sm == target:
#                     return True
#                 return False
            
#             return dp(i + 1,sm + nums[i]) or dp(i + 1,sm)
        
        
#         return dp(0,0)

        
        cache = [[False] * (target + 1) for _ in range(N)]
        
       
        for i in range(N):
            cache[i][0] = True
      
        cache[0][nums[0]] = True
        
        for i in range(1,N):
            for sm in range(1,target + 1):
                leave = False
                if sm - nums[i] >= 0:
                    leave = cache[i - 1][sm - nums[i]]
                cache[i][sm] = cache[i - 1][sm] or leave
                        
        return cache[N - 1][target // 2]
                
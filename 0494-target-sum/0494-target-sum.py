class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dp(i,sm):
            
            if i >= len(nums):
                if sm == 0:
                    return 1
                else:
                    return 0
            
            return dp(i + 1,sm + nums[i]) + dp(i + 1,sm - nums[i])
            
        
        return dp(0,target)
        
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        target = total // 2
        N = len(nums)
        @cache
        def dp(i,sm):
            if i >= N:
                if sm == target:
                    return True
                return False
            
            return dp(i + 1,sm + nums[i]) or dp(i + 1,sm)
        
        
        return dp(0,0)
                
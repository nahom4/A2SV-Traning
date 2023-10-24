class Solution:
    def jump(self, nums: List[int]) -> int:
        #let's first do it to down then we will do bottom up
        @cache
        def dp(i):
            N = len(nums)
            if i >= N - 1:
                return 0
            mn = float("inf")
            for val in range(1,nums[i] + 1):
                mn = min(dp(i + val),mn)
                
            return mn + 1
        
        return dp(0)
            
            
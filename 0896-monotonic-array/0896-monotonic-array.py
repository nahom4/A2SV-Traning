class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        def isMonoton(nums):
            N = len(nums)
            for i in range(N - 1):
                if nums[i + 1] < nums[i]:
                    return False
            return True
        return isMonoton(nums) or isMonoton(nums[:: -1])
                
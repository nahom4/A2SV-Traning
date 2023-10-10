class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        N = len(nums)
        nums = list(set(nums))
        minOpperations = N
        nums.sort()
        for i in range(len(nums)):#2 3 4 5
            left = nums[i]
            right = left + N - 1
            rightBound = bisect.bisect_right(nums,right)
            minOpperations = min(minOpperations,N - (rightBound - i))
             
        return minOpperations
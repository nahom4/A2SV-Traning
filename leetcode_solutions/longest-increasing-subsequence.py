class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp
        N = len(nums)
        cache = [1] *  N
        for i in range(N):
            maxValue = 0
            for j in range(i - 1,-1,-1):
                if nums[i] == 7:
                    print(nums[i],nums[j])
                if nums[j] < nums[i]:
                    maxValue = max(maxValue,cache[j])
               
            cache[i] += maxValue
        return max(cache)

        
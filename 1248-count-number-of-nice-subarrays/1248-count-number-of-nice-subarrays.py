class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        size = len(nums)
        for i in range(size):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
                
        
        #problem reduced to number of subarray sum == k
        def sum_less(k,nums):
            #no of subarray sum less than k
            size = len(nums)
            left = 0
            result = 0
            curr_sum = 0
            for i in range(size):
                curr_sum += nums[i]
                
                while left <= i and curr_sum > k:
                    curr_sum -= nums[left]
                    left += 1
                
                result += i - left + 1
            return result
        return sum_less(k,nums) - sum_less(k-1,nums)
        
                
                
            
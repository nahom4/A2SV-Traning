class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def subarray_counter(nums,k):
            
            n = len(nums)
            count = 0
            running_sum = 0 
            left = 0
            
            for right in range(n):
                
                running_sum += nums[right]
                
                while left <= right and running_sum > k:
                    running_sum -= nums[left]
                    left += 1
                    
                
                count += right - left + 1
            return count
        return subarray_counter(nums,goal) - subarray_counter(nums,goal - 1)
   
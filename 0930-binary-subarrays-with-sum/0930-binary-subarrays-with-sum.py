class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
         def sub_sum(nums,goal):
            #count number of ones
            left = 0
            count =  0
            result = 0

            for right in range(len(nums)):
                count += nums[right]

                while left <= right and count > goal:

                    count -= nums[left]
                    left += 1

                result += right - left + 1

            return result
        
         return sub_sum(nums,goal) - sub_sum(nums,goal - 1)
       
   
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        #we are doing a cyclic sort but jumping elements that doesn't sutisfy the property 
        #of being > 0 and < len(nums)
        left = 0
        while left < len(nums):
            
            if nums[left] <= 0 or nums[left] > len(nums) or nums[left] == nums[nums[left] - 1]:
                left += 1
                continue
                
            
            index = nums[left]
            nums[left],nums[index - 1] = nums[index - 1],nums[left]     
            
            if nums[left] - 1 == left:
                left += 1
                
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1
        return len(nums) + 1
                
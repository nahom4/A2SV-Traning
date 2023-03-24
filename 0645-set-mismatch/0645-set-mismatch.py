class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        left = 0
        result  = []
        while left < len(nums):
            index = nums[left]
            if nums[left] == nums[nums[left] - 1]:
                left += 1
                continue
            nums[index - 1],nums[left] = nums[left],nums[index - 1]
            if left == nums[left] -1 :
                left += 1
        
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                result.append(nums[i])
                result.append(i + 1)
        return result
        
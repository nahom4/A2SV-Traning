class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums = self.quick(nums)
        arr = []
        for x in range(len(nums)):
            if nums[x] == target:
                arr.append(x) 
        return arr
    
    def quick(self,nums):
        
        if len(nums)<=1:


            return nums
        left = []
        right = []
        pivot = nums.pop()
       
        for x in nums:
            if x <= pivot:
                left.append(x)
            else:
                right.append(x)
        
        return self.quick(left)+[pivot]+self.quick(right)

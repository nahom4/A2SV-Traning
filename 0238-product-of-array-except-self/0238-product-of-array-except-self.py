class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #prefix product from the start and the end excluding the current elements
        size = len(nums)
        #forward
        forward = [1]*size
        for i in range(size-1):
            forward[i + 1] = nums[i]*forward[i]
            
        #backward
        backward = [1]*size
        for i in range(size - 1,0,-1):
            backward[i - 1] = nums[i] * backward[i]
            
        #product
        new = []
        for i in range(size):
            new.append(forward[i]*backward[i])
            
        return new
            
        
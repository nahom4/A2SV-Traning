class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def count_less(value):
            
            less = 0
            
            for i in range(len(nums)):
                if nums[i] <= value:
                    less += 1
                    
            return less > value
        
        
        low = 0
        high = len(nums)
        
        while high > low + 1:
            md = low +  (high - low) // 2
            
            if count_less(md):
                high = md
            else:
                low = md
                
        return high
        
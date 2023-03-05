class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = -1
        high = len(nums)
        
        while high > low + 1:
            
            md = low + (high - low)//2
            
            if nums[md] >= target:
                high = md
            else:
                low = md
                
        return high
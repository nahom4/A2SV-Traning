class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        #search for the first element greater or equla to target and strictly greater than target
        
        #greater or equla
        def greater_equal(value):
            
            low = -1 
            high = len(nums)
            
            while high > low + 1:
                
                md = low + (high - low)//2
                
                if nums[md] >= value:
                    high = md
                else:
                    low = md
                    
            return high
        
        def greater(value):
            low = -1
            high = len(nums)

            while high > low + 1:
                
                md = low + (high - low)//2
                
                if nums[md] > value:
                    high = md
                else:
                    low = md
            return low
        start = greater_equal(target)
        end = greater(target)
        if start > end:
            return [-1,-1]
        return [start,end]
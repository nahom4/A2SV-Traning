class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        
        def havePPairs(limit):
            i = 0
            count = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= limit:
                    count += 1
                    i += 1   
                i += 1
            return count 
    
        left,right = 0,(nums[-1] - nums[0])
        
        while left < right:
            
            md = left + (right - left) // 2

            if havePPairs(md) >= p:
                right = md
                
            else:
                left = md + 1
                
        return left
            
                    
                
                    
                
        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #add
        #validate
        #remove
        #update
        
        size = len(nums)
        left = 0
        
        curr_sum = 0
        min_length = size
        is_valid = False
        
        for right in range(size):
            
            #add
            curr_sum += nums[right]
            
            #validate
            while curr_sum >= target:
                is_valid = True
            
                curr_sum -= nums[left]
                min_length = min(min_length,right - left + 1)
                left += 1
            
        if not is_valid:
            return 0
                
           
        
        return min_length
            
            
            
            
        
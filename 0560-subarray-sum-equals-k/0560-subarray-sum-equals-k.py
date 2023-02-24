class Solution:

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum  = defaultdict(int)
        prefix_sum[0] = 1
        total = 0
        result = 0
        
    
        for i in range(len(nums)):
            
            total += nums[i]
            #we have found a prefix that can be removed to make the new prefix valid
            if prefix_sum[total - k] != 0:
                
                result += prefix_sum[total - k]
            prefix_sum[total] += 1
        return result
                
                
                
            
            
        
        
    
             
        
        
        
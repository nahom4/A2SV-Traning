class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #add
        #validate
        #update
        n = len(nums)
        
        left =  0
        result = float("-inf")
        curr_sum = 0
        
        if k == n:
            return sum(nums)/k
        
        for right in range(n):
            curr_sum += nums[right]
            
            if right >= k:
                curr_sum -= nums[left]
                left += 1
                
            if right + 1 >= k:
                
                result = max(result,curr_sum)
            
        return result/k
                
                
        
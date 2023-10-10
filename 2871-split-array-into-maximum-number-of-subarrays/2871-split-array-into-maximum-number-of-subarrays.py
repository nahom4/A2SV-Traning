class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = list(nums)
        for i in range(N - 2,-1,-1):
            prefix[i] &= prefix[i + 1]
           
        minScore = prefix[0]
        prefix.append(float("-inf"))
        currScore = -1
        ct = 0
        for i in range(N):
            
            if currScore == -1:
                currScore = nums[i]
                
            else:
                currScore &= nums[i]
            
            if currScore + prefix[i + 1] <= minScore:
                ct += 1
                currScore = -1
                
        
        return ct
                
                
                
                
                
            
            
        
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        #The key here is the range we want the biggest value to be in the most
        #optimal position so that it can be added the most
        ans = [0]*(len(nums) + 1)
        modulo = 10**9 + 7
        for request in requests:
            
            start,end = request
            
            ans[start] += 1
            ans[end + 1] -= 1
       
        #do prefix sum
        ans.pop()
      
        for i in range(1,len(nums)):
            
            ans[i] += ans[i - 1]
          
    
        ans.sort(reverse=True)
        nums.sort(reverse=True)
            
        result = 0
        
        for num,count in zip(ans,nums):
            result += num * count
        
        return result % modulo
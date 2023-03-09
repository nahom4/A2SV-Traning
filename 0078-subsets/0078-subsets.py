class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        ans = []
        
        #the problem is finding combinations of size k
        
        
        def comb(index,k):
            
            if len(ans) == k:
                result.append(list(ans))
                return
            
            if index >= len(nums):
                return
            
            comb(index + 1,k)
            ans.append(nums[index])
            comb(index + 1,k)
            ans.pop()
            
        for i in range(0,len(nums) + 1):
            comb(0,i)
        
        
        return result
            
        
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = [0]*len(nums)
        result = []
        
        def backtrack(nums,index):
            
            if len(nums) == 0:
                result.append(list(ans))
                return 
            
            for i in range(len(nums)):
                ans[index] = nums[i]
                new = list(nums)
                new.remove(nums[i])
                backtrack(new,index + 1)
                
        backtrack(nums,0)
        return result
            
        
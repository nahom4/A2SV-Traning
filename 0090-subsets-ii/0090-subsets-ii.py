class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        ans = []
        nums.sort()
        #the problem is finding combinations of size k
        
        
        def comb(index):
             
            if index >= len(nums):
                result.append(ans[::])
                return
            
            ans.append(nums[index])
            comb(index + 1)
            ans.pop()
            
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            comb(index + 1)
           
            
        comb(0)
        return result
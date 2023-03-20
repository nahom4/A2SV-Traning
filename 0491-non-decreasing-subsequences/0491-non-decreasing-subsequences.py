class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        curr = []
        result = set()
        
        def backtrack(index):
            
            if len(curr) >= 2:
              
                result.add(tuple(curr))
                
            if index >= len(nums):
                return
            
            if not curr or curr[-1] <= nums[index]:
                curr.append(nums[index])
                backtrack(index + 1)
                curr.pop()
            
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1)
            
        backtrack(0)
        
        return result
                
            
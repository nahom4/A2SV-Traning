class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        mx = 0
        #generate all possible subsets
        curr = []
        for num in nums:
            mx = mx | num
        
        nums.sort()
        def backtrack(index):
            nonlocal count
            value = 0
           
            if index >= len(nums):
                
                for num in curr:
                    value = value | num
                if value == mx:
                    count += 1
                return
            
           
            curr.append(nums[index])
            backtrack(index + 1)
            curr.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return count
        
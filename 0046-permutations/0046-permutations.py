class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = [0]*len(nums)
        result = []
        num = 0 
        
        def backtrack(index):
            nonlocal num
            if index >= len(nums):
                result.append(list(ans))
                return 
            
            for i in range(len(nums)):
                #check here if this number has been used at a particular index
                start = 1
                count = i
                while count > 0:
                    start = start << 1
                    count -= 1
                
                if num & start == 0 or num == 0:
                   
                    ans[index] = nums[i]
                    num = num | start
                    backtrack(index + 1)
                    num = num ^ start
                    
                    
        backtrack(0)
        return result
            
        
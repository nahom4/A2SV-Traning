class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        mn = float('-inf')
        stack = []
        
        for index in range(len(nums) - 1,-1,-1):
            
            if nums[index] < mn:
                return True
            
            while stack and stack[ -1 ] < nums[index]:
                mn = stack.pop()
                
            stack.append(nums[index])
        
       
        
        
        
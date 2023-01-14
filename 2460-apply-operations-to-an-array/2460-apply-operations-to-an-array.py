class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        #let's use two pointer to push the zeros to the end
        
        
        for i in range(len(nums)-1):
            
            if nums[i] ==  nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        left = 0
        flag = True
        j = 0
       
        for i,x in enumerate(nums):
            
            if flag and nums[left] == 0:
                
                
                
                flag = False
            if not flag and x > 0:
                nums[left],nums[i] = nums[i],nums[left]
                flag = True
                
            if flag:
                left+=1
            
              
                
                
        return nums
                
                
        
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        
        index = 0
        right = len(nums)-1
        
      
        
        for i in range(len(nums)):
            
            if nums[i] < 0:
                index = i
            
            nums[i] = nums[i]**2
        
        result = []
        left = index 
        right = index + 1
        
        if len(nums) <= 1:
            return nums
        
     
        
        
        while left >=0 and  right < len(nums):
            
     
        
            if nums[left] == nums[right]:

                result.append(nums[left])
                result.append(nums[left])

                left-=1
                right +=1
            elif nums[left] < nums[right]:
                result.append(nums[left])
                left-=1
            else:
                result.append(nums[right])
                right += 1
   
                
        while left >=0:
                result.append(nums[left])
                left-=1
        while right < len(nums):
                result.append(nums[right])
                right += 1
            
            
        return result
    
        
        
            
        
        
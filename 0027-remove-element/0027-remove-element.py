class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        end = len(nums)-1
        if not nums:
            return len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            
            if nums[i] == val:
                nums[end], nums[i] = nums[i],nums[end]
                end-=1
                
        return len(nums[:end+1])
            
        
      
        
       

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        
        dic = dict()
        for i in range(len(nums)):
            dic[(i+k)%len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i]= dic[i] 
            
            
            
            
            
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        read = write = 0
        N = len(nums)
        
        for read in range(N):
            
            if nums[read] != 0:
                nums[read],nums[write] = nums[write],nums[read]
                
            if nums[write] != 0:
                write += 1
                
        
        
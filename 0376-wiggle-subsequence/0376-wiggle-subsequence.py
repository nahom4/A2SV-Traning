class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return len(nums)
        cache = {}
        
        def helper(i):
            
            value,parity,size = cache[i + 1]
            
            if value - nums[i] == 0:
                return (nums[i],parity,size)
            
            elif parity == -1:
                return (nums[i],True if nums[i + 1] - nums[i] > 0 else False,2)
            
            elif value - nums[i] > 0 and parity:
                return (min(value,nums[i]),parity,size)
            elif value - nums[i] < 0 and not parity:
                return (max(value,nums[i]),parity,size)

            
            else:
                return (nums[i],not parity,size + 1)
            
            
        cache[len(nums) - 1] = (nums[-1],-1,1)
        for i in range(len(nums) - 2,-1,-1):
            cache[i] = helper(i)
            
        return cache[0][2]
            
            
            
            
        
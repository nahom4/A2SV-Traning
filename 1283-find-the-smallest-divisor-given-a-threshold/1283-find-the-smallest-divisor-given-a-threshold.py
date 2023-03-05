class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        sm = sum(nums)
        #our binary search space is the range between 1 and sm
        
        low = 0
        high = sm + 1
        def valid(value):
            running_sum = 0
            for i in range(len(nums)):
                running_sum += ceil(nums[i]/value)
                
            return running_sum
                
        
        while high > low + 1:
            
            md = low + (high - low)//2
            if valid(md) <= threshold:
                high = md
            else:
                low = md
        return high
        
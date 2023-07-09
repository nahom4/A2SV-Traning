class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cache = defaultdict(int)
        def dp(sm):
            
            if sm == target:
                return 1
            if sm > target:
                return 0
            
            if sm in cache:
                return cache[sm]
            count = 0
            for num in nums:
                
                count += dp(sm + num)
                
            cache[sm] = count
            return count
        
        return dp(0)
            
            
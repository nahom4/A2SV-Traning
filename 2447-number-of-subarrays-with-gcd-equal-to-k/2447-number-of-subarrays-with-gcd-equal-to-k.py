class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        def gcd(sm,mx):
              #base case
            if sm  == 0:
                return mx
            return gcd(mx % sm, sm)
            
    
        i = 0
        while i < len(nums):
            j = i
            gcd_value = 0
            while j < len(nums):
                gcd_value = gcd(gcd_value,nums[j])
                if gcd_value == k:
                    count += 1
                elif gcd_value < k:
                    break
                
                j+= 1
            i += 1
        
        return count
        
                
            
        
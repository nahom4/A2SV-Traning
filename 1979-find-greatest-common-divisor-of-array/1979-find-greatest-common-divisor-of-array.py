class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        #gcd recursively calls the gcd function with the smaller number and the remainder of division of the large
        #number and the smaller number
        mx = max(nums)
        sm = min(nums)
        
        def gcd(sm,mx):
            
            #base case
            if sm  == 0:
                return mx
            return gcd(mx % sm, sm)
        
        return gcd(sm,mx)
        
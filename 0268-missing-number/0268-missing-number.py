class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        #let's prepare a dictionary indicating the presence of a number
        presence = dict()
        
        for x in nums:
            presence[str(x)] = 1
            

                
                
        for check in range(len(nums)+1):
            value = presence.get(str(check),0)
            if value == 0:
                return check
            
        
        
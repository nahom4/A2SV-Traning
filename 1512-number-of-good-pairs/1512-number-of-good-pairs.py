class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        #first lets count each element
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0)+1
        sm = 0    
        for value in count:
            
            res = count[value] -1
            
            sm+=(res+res**2)//2
            
        return sm
            
         
        
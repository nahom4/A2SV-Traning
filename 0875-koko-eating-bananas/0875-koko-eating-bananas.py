class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            running_sum = 0
            
            for i in range(len(piles)):
                
                running_sum += ceil(piles[i] / k)
            return running_sum
        
        #our binary search space is between  1 and max(piles) right is a 1 and represents <= h and left is > h and represented as 0
        
        low = 0
        high = max(piles) + 1
        
        
        while high > low + 1:
            
            md = low + (high - low )//2
          
            if check(md) <= h:
                high = md
            else:
                low = md
                
                
        return high
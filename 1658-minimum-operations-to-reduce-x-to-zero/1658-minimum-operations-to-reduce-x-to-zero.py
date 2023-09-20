class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        N = len(nums)
        sm = 0
        start = float("inf")
        for i in range(N):
            sm += nums[i]
            if sm >= x:
                start = i
                break
                
        if start == float("inf"):
            return -1 
        right = N
        minValue = float("inf")
        """
            [1,1,3,2,5]
            1,2,5,7,12
            0,1,2,3,4

        """
    
        while start >= 0 or right >= 0:
              
            while sm <= x:
    
                if sm == x:
                    minValue = min(minValue,(start + 1 + (N - right)))
                 
                right -= 1
                sm += nums[right]
                
            sm -= nums[start]
            if start < 0:
                break
           
            start -= 1
            
        return -1 if minValue == float("inf") else minValue
                
            
          
               
    
       
                
        
       
          
                
        
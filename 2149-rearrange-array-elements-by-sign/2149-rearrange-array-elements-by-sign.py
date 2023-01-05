class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        #prepare a positive and a negative array
        
        positive = []
        negative = []
        for x in nums:
            if x < 0:
                negative.append(x)
            if x > 0:
                positive.append(x)
      
        
        new = []
                
        for i in range(len(positive)):
            new.append(positive[i])
            new.append(negative[i])
            
            
            
            
            
           
        return new
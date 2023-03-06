class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        low = 0
        high = max(citations) + 1
        n = len(citations)
        
        def validate(value):
            low = -1
            high = len(citations)
            
            while high > low + 1:
                md = low + (high - low) // 2
                
                if citations[md] >= value:
                    
                    high = md
                else:
                    low = md
            return high
        
        
        while high > low + 1:
            
            md = low + (high - low)//2
            
            if  n - validate(md)  >= md :
                low = md
                
             
            else:
                high = md
                
          
        return low
              
          
      
        
import numpy



class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        lis = []
        
        for x in strs:
            temp = []
            for char in x:
                temp.append(char)
            lis.append(temp)
            
 
            
       
        new = numpy.transpose(lis)
        result = []
        
        
        for row in range(len(new)):
            valid = True
            for char in range(1,len(new[0])):
                
                if new[row][char] < new[row][char-1]:
                    valid = False
                    
                else:
                    continue
                   
            if valid:
                
                result.append(new[row])
                
      
        
   
                      
        return len(new) - len(result)
        
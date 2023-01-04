class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        #we should treat as a matrix problem and traverse the matrix column wise
        # to do that we should keep the colcumn constant and change the row
        # we should also know the length of each word
        
        s = s.split()
        
        length = [len(n) for n in s]
        mx = max(length)
        
        final = []
        
        for col in range(mx):
            text = ""
            for row in range(len(s)):
                
                
                
                if length[row] > col:
                    
                    text+= s[row][col]
                else:
                    text+= " "
                    
            final.append(text.rstrip())
            
        return final
                    
                    
            
                    
                
                
        
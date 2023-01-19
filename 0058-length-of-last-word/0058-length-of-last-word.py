class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        word = ''
   
        s = s.rstrip()
      
        
        for x in s:
            
            if x!=" ":
               
                word+=x
            else:
                word=""
                
        return len(word)
                
      
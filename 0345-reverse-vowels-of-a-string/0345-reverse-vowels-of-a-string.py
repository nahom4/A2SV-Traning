class Solution:
    def reverseVowels(self, s: str) -> str:
        
        #Two pointers
        
        left = 0
        right = len(s) -1
        
        vowles = ["a","e","i","o","u","A","E","I","O","U"]
        
        s = list(s)
     
        
        while left< right:
            
            while not s[left] in vowles and left < right:
              
                left+=1
            
            
            while not s[right] in vowles and left < right:
                
               
                right-=1
                
           
                
            s[left],s[right] = s[right],s[left]
            
            left+=1
            right-=1
    
                
        return ''.join(s)    
            
            
        
class Solution:
    def freqAlphabets(self, s: str) -> str:
        #there are two types of numbers a single digit and double digit that will 
        #be followed by a hash
        
        
        i = 0
        line = ""
        while i < len(s):
            
            #check for a single number
            if i+2>len(s)-1 or s[i+2] != "#":
                line += chr(int(s[i]) + 96)
            
                i+=1
            #check for doble digit:
            else:
                j = i+2
                line += chr(int(s[i:j]) +96)
             
                i+=3
                
        return line
                
                
                
            
        
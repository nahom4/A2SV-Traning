class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new = []
        
        count = 0 #counts the number of spaces added
        
        
        for i in range(len(spaces) + len(s)):
            if count < len(spaces) and spaces[count]+ count == i:
                new.append(" ")
                count+=1
            else:
                new.append(s[i-count])
      
        return "".join([n for n in new])
            
        
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        size = len(s)
        dic = dict()
        result = []
        #let use a stack to solve the problem and dictionary to track repeated values
        for i in range(size):
            dic[s[i]] = i
            
        for i, letter in enumerate(s):
           
         
            if letter not in result:
          
                while result and dic[result[-1]] > i and letter < result[-1]:
                    result.pop()
                    
                result.append(letter)

              
            
         
        return ''.join(result)
            
        
            
            
        
        
      
                    
        
      
        
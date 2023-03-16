class Solution:
    def decodeString(self, s: str) -> str:
        
        # we first need to now matching squere brackets
        stack = []
        dic = dict()
        
        for index, p in enumerate(s):
            
            if p == '[':
                stack.append(index)
            elif p == ']':
                dic[stack.pop()] = index
        
        def decode(s,mul_number,left,right):
        
            if '[' not in s[left : right + 1]:
              
                return s[left : right + 1] * int(mul_number)
                
            
            #I am looking for a number and an open brace
            result = ''
            number = ''
            while left <= right:
               
                if s[left].isnumeric():
                    number += s[left]
                   
                    left += 1
                
                elif s[left] == '[':
                  
                    result += decode(s,number,left + 1,dic[left] - 1)
                    number = ''
                   
                    left = dic[left]
                    
                else:
                    
                    if not s[left].isnumeric() and s[left] != '[' and s[left] != ']':
                            
                            result += s[left]
                    left += 1
                    
            return int(mul_number) * result
        return decode(s,1,0,len(s) - 1)
                    
                    
                    
                
                
            
                
        
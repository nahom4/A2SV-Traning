class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = []
        def sequence(num):
            
            if len(num) == 0:
                
                return len(ans) >= 3
            
            for left in range(len(num)):
              
                digit = num[:left + 1]
                if len(digit) >= 2 and int(digit[0]) == 0:
                    pass
                else:
                  
                       
                    if len(ans) <= 1 or (int(ans[-1]) + int(ans[-2])) == int(digit):
                        ans.append(digit)
                        if sequence(num[left + 1:]):
                            return True
                        else:
                            ans.pop()
                        
            return False
                  
                    
                    
                   
        return sequence(num)
                    
                
                
                
                
            
        
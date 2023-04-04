class Solution:
    def countArrangement(self, n: int) -> int:
       
        ans = []
        result = 0
        num = 0 
 
        def backtrack(index):
            nonlocal n
            nonlocal result
            nonlocal num
           
            if  len(ans) == n:
                result += 1
                return 
            
            if index > n:
                return
            
            for i in range(1,n + 1):
                #check here if this number has been used at a particular index
             
                start = 1
                start = start << i
                
                
                if (num & start == 0 or num == 0) and ((index % i == 0) or (i % index == 0)):
                   
                    ans.append(i)
                    num = num | start
                    backtrack(index + 1)
                    num = num ^ start
                    ans.pop()
                  
                    
                    
        backtrack(1)
        return result
        
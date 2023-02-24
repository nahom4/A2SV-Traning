class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        size = len(temperatures)
        result = [0]*size
        for i in range(size):
            
            #before we add to a stack check if it is decreasing
            if len(stack) == 0 or stack[-1][0] >= temperatures[i]:
                stack.append([temperatures[i],i])
                continue
              
            
         
            while stack and stack[-1][0] < temperatures[i]:
            
                value = stack.pop()
                
             
                result[value[1]] = i - value[1]
        
            stack.append([temperatures[i],i])
                
        return result
            
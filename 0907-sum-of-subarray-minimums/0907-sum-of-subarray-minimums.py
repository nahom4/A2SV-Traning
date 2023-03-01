class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        incr_stack = []
        result_stack = []
        final_result = 0
        modulo = 10 ** 9 + 7
        
        for i in range(len(arr)):
            
            
            
            while incr_stack and arr[i] <= arr[incr_stack[-1]]:


                incr_stack.pop()
                result_stack.pop()
                
            if not incr_stack:
                incr_stack.append(i)
                result_stack.append((i + 1) * arr[i])
                final_result += result_stack[-1]
            else:

                result_stack.append((result_stack[-1] + (i - incr_stack[-1]) * arr[i]))
                incr_stack.append(i)
                final_result += result_stack[-1]

        return final_result % modulo
                
                
                
        
            
            
        
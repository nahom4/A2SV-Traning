class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        
        result = 0
        stack =  []
        for p in s:
            
            if p == '(':
                stack.append(0)
                
            else:
                mul = stack.pop()
                if mul == 0:
                    val = 1
                else:
                    val = 2 * mul
                    
                if not stack:
                    result += val
                    
                else:
                    stack[-1] += val
                    
        return result
        
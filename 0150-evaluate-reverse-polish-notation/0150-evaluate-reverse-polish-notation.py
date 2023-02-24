class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opertators = ['+','-','*','/']
        
        for i in range(len(tokens)):
            
            if tokens[i] in  opertators:
                second = int(stack.pop())
                first = int(stack.pop())
                
                if tokens[i] == '+':
                    
                    result = first + second
                elif tokens[i] == '*':
                       result = first * second
                elif tokens[i] == '/':
                    
                    result = first / second
                      
                       
                elif tokens[i] == '-':
                       result = first - second
                stack.append(result)
            else:
                stack.append(tokens[i])
                
        return int(stack[0])
            
        
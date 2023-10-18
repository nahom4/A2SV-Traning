class Solution:
    def calculate(self, s: str) -> int:
        
        opperations = []
        num = []
        s = s.replace(" ","")
        N = len(s)
        for i in range(N):
            if not s[i].isdigit():
                opperations.append("".join(num))
                opperations.append(s[i])
                num = []
            else:
                num.append(s[i])
        if num:
            opperations.append("".join(num))
        
        #multiplication and division
        stack = []
        for value in opperations:
            
            if stack and (stack[-1] == "*" or stack[-1] == "/"):
                sign = stack.pop()
                a = stack.pop()
                if sign == "*":
                    stack.append(int(a) * int(value))
                else:
                    stack.append(int(a) // int(value))
                    
            else:
                stack.append(value)
         
        print(stack)
        #addition and substraction
        stack2 = []
        for value in stack:
            if stack2 and (stack2[-1] == "-" or stack2[-1] == "+"):
                sign = stack2.pop()
                a = stack2.pop()
                if sign == "+":
                    stack2.append(int(a) + int(value))
                else:
                    stack2.append(int(a) - int(value))
                    
            else:
                stack2.append(value)

        return int(stack2[0])
                
        
                
        
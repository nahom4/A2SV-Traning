class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def backSpace(string):
            
            stack = []
            
            for letter in string:
                
                if stack and letter == '#':
                    stack.pop()
                elif letter != "#":
                    stack.append(letter)
                    
            return stack
        return backSpace(s) == backSpace(t)
    
                    
        
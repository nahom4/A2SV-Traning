class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        N = len(asteroids)
        
        for i in range(N):
            
            if asteroids[i] > 0:
                stack.append(asteroids[i])
                
            else:
                
                while stack and stack[-1] > 0 and asteroids[i] < 0 and abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                    
                if stack and stack[-1] > 0 and abs(stack[-1]) > abs(asteroids[i]):
                    continue
                elif stack and stack[-1] > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                else:
                    stack.append(asteroids[i])
                    
        return stack
            
 
        
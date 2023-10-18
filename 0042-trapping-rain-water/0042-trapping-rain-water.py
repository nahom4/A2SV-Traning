class Solution:
    def trap(self, height: List[int]) -> int:
        
        #let's try a monotonic stack
        
        stack = []
        total = 0
        N = len(height)

        for i in range(N):
            curr = height[i]
            while stack and stack[-1][0] <= curr:#sink
                top = stack[-1]
                maxHeight = top[2]
                runningTotal = (top[0] - maxHeight) * (i - top[1] - 1)
                total += runningTotal
                stack.pop()
                
            if stack:
                top = stack[-1]
                diff = curr - top[2]
                total += diff * (i - stack[-1][1] - 1)
                stack[-1][2] = max(curr,stack[-1][2])
                
                
            stack.append([curr,i,0])
            
        
        return total
            
                
                
                
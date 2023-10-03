class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #let's use a stack to solve this problem
        stack = []
        N = len(s)
        for i in range(N):
            letter = s[i]
            ct = 1
            if stack and stack[-1][0] == letter:
                ct += stack[-1][1] 
                
            stack.append((letter,ct))
            
            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
                             
        return "".join(list(map(lambda x : x[0],stack)))        
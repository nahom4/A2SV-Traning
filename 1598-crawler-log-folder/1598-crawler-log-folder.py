class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for operation in logs:
            #operation are d/ ,../ ./
            if operation == './':
                pass
            elif operation == '../':
                if stack:
                    stack.pop()
            else:
                stack.append(operation)
                
        return len(stack)
            
        
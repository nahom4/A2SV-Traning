class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        curr = []
        max_length = 0
        
        def backtrack(index):
            nonlocal max_length
            max_length = max(max_length,len(''.join(curr)))
            if index >= len(arr):
                return 
            
            curr.append(arr[index])
            
            if len(''.join(curr)) == len(set(''.join(curr))):
                backtrack(index + 1)
                
            curr.pop()
            backtrack(index + 1)
        backtrack(0)
        return max_length
        
from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        
        final = float('inf')
        temp = 0
        store = deque()
        sm = 0
        for right in range(len(nums)):
            
            sm += nums[right]
            
            if sm >= k:
                final = min(final,right + 1)
            
            
            while store and sm - store[0][1] >= k:
                final = min(final,right - store[0][0])
                store.popleft()
                
            while store and store[-1 ][1] > sm:
                store.pop()
                
            store.append([right,sm])
        
        return -1 if final == float('inf') else final
                
            
            
        
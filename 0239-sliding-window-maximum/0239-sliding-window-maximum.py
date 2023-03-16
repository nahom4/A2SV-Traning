from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        inc_queue = deque()
        inc_queue_index = deque()
        left = 0
        result = []
        for right, num in enumerate(nums):
            while inc_queue and inc_queue[ -1 ] < num:
                inc_queue.pop()
                inc_queue_index.pop()
             
           
            inc_queue.append(num)
            inc_queue_index.append(right)
           
            
            if right - left + 1 >= k:

                result.append(inc_queue[0])
            
                if inc_queue and inc_queue_index[0] == left:
                    inc_queue.popleft()
                    inc_queue_index.popleft()
                left += 1
                    
        return result
            
        
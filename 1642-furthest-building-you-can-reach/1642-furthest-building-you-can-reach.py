class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        n = len(heights)
        usedBricks = 0
        for i in range(1,n):
            heightDifference = heights[i] - heights[i - 1]
            if heightDifference <= 0:
                continue
                
            heapq.heappush(heap,heightDifference)    
            if len(heap) > ladders:
                usedBricks += heapq.heappop(heap)
                
            if usedBricks > bricks:
                return i - 1
            
        return n - 1
                
      
                
                
                
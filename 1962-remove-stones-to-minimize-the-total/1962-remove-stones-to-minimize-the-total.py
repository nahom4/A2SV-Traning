class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [- value for value in piles]
        heapq.heapify(piles)
        
        
        for _ in range(k):
            
            biggest = heapq.heappop(piles)
            biggest = -biggest
            
            heapq.heappush(piles,-(ceil(biggest / 2)))
            
            
        return -sum(piles)
        
        
        
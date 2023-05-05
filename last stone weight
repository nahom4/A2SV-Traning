class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda value : -value,stones))
        heapq.heapify(stones)
      
        while len(stones) > 1:
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)
            if first != second:
                heapq.heappush(stones,-(max(first,second) - min(first,second)))
                
        if stones:
            return -stones.pop()
        
        return 0
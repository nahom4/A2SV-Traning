class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        heap = []
        heapq.heapify(heap)
        n = len(matrix)
        heapSize = n ** 2 - k + 1
        
        for i in range(n):
            for j in range(n):
                
                currentElement = matrix[i][j]
                
                if len(heap) >= heapSize:
                    smallestElement = heapq.heappop(heap)
                    
                    if smallestElement > currentElement:
                        currentElement = smallestElement
                        
                    heapq.heappush(heap,currentElement)
                        
                else:
                    heapq.heappush(heap,currentElement)
    
        kthLargest = heapq.heappop(heap)
        return kthLargest
            
        
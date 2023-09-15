class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #let's try prims algorithm
        visited = set()
        heap = [(0,0, 0)]
        N = len(points)
        
        def  manhattanDistance(pointA,pointB):
            xA,yA = pointA
            xB,yB = pointB
            
            return abs(xA - xB) + abs(yA - yB)
        
        minCost = 0
        while len(visited) < N:
            distance,pointA,pointB = heapq.heappop(heap)
            
            if not pointB in visited:
                minCost += distance
                visited.add(pointB)
                for i in range(N):
                    if not i in visited:
                                heapq.heappush(heap,(manhattanDistance(points[pointB],points[i]),pointA,i))

        return minCost
            
    
        
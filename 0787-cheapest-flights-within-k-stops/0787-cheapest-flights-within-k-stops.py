class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)
        for start,finish,cost in flights:
            graph[start].append((finish,cost))
            
        
        priorityQueue = [(0,src,0)] #cost node stops
        visited = set()
        """
            4
            [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
            0 start
            3 des
            1 k
        """
        while priorityQueue:
            cost,node,stops = heapq.heappop(priorityQueue)# k = 1 
            if node == dst:
                return cost
            
            if (node,stops) in visited:
                continue
                
            visited.add((node,stops))
                    
            for child,currCost in graph[node]:
                if stops <= k:
                    heapq.heappush(priorityQueue,(currCost + cost,child,stops + 1))
        
        return -1
                    
            
                    
                
                
                
            
             
        
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        visited = set()
        heap = [(-1,start_node)]
        
        graph = defaultdict(list)
        for i in range(len(edges)):
            start,end = edges[i]
            prob = succProb[i]

            graph[start].append((end,prob))
            graph[end].append((start,prob))
        
        while heap:
            prob,node = heapq.heappop(heap)
            if node == end_node:
                return -prob
            if node in visited:
                continue
                
            visited.add(node)
            
            for child,childProb in graph[node]:
                heapq.heappush(heap,((prob * childProb),child))
                        
        return float(0)
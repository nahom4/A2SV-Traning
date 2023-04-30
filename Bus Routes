class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        graph = defaultdict(list)
        visited = set()
        res = -1
        queue = deque()
        reached = False
        
        for index,loop in enumerate(routes):
            for city in loop:
                graph[city].append(index)
         
        
        
        for index,loop in enumerate(routes):
            
            if source in loop:
                queue.append(index)
                visited.add(index)
        
        res = 0 
        if source == target:
            return res
        while queue:
            
            res += 1
            size = len(queue)
            
            for _ in range(size):
                bus_no = queue.popleft()
                for city in routes[bus_no]:

                    if city == target:
                        reached = True
                    
                    if reached:
                        break
                    for val in graph[city]:
                        if not val in visited:
                            visited.add(val)
                            queue.append(val)
            if reached:
                    break
        return res if reached else -1
                    
            
            
            
                
            
     
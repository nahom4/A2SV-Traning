class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        #let's build a graph
        graph = defaultdict(list)
        visited = set()
        for edge in edges:
            
            start,end = edge
            graph[start].append(end)
            graph[end].append(start)
  
        def dfs(node):
        
            visited.add(node)
            #a node might have an apple or it might lead to one either way it neads to be take
            has_apple = hasApple[node]
            
            total = 0
         
            for child in graph[node]:
                if child not in visited:
                    #does this child lead to an apple so res 
                    res = dfs(child)
                    total += res
             
            if node == 0:
                return total
            
            if has_apple or total > 0:
                total += 2
                    
            return total
        
        return dfs(0)
                
                
            
            
        
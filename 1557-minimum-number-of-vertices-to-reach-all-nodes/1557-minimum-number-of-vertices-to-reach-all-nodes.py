class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        print(edges)
        
        
        graph = defaultdict(list)
        nodes = set()
        for edge in edges:
            start,goal = edge
            nodes.add(start)
            nodes.add(goal)
            graph[start].append(goal)
        
       
      
        values = []     
        for key in graph:
            
            values += graph[key]
            
        values = set(values)
        ans = []
        for key in nodes:
            if key not in values:
                ans.append(key)
                
        return ans
            

                    
                
                
        
        
        
      
        
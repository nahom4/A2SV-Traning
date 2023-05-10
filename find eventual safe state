class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        #if a possible path contains a cycle then we don't register the node
        # that generated the path
        
        #let's create the graph actaully we don't need to create the graph
        queue = deque()
        color = [0] * len(graph)
        res = []
    
        def dfs(node):
    
            if color[node] == 1:
                return False
            
            color[node] = 1
            
            valid = True
            for child in graph[node]:
                #if there was any cycle along the path the node won't be valid
                if color[child] != 2 and color[child] != -1:
                    valid = valid and dfs(child)
                    
                if color[child] == -1:
                    valid = False
          
            if valid:
            
                color[node] = 2
                res.append(node)
                return True
            color[node] = -1
           
            return False
                
            
        for node in range(len(graph)):
            
            if color[node] != 0:
                continue  
            
            dfs(node)
            
        res.sort()
        return res

            
        
               
            
            
       
class Solution:
    longest_cycle = float('-inf')
    def longestCycle(self, edges: List[int]) -> int:
  
        color = [0] * len(edges)
        location = {}
        
        def dfs(node):
                color[node] = 1
                child = edges[node]
                if child != -1:
                    if color[child] == 0:
                        location[child] = location[node] + 1
                        dfs(child)

                    if color[child] == 1: # this means a cycle
                   
                        self.longest_cycle = max(self.longest_cycle ,location[node] - location[child] + 1)
          
        
                color[node] = 2
            
        for node in range(len(edges)):
            
            if color[node] != 0:
                continue  
            location = {}
            location[node] = 0
            dfs(node)
            
      
        return -1 if self.longest_cycle == float('-inf') else self.longest_cycle
        
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        path = []
        target = len(graph) - 1
        result = []
        
        def dfs(index):
         
            path.append(index)
            if index == target:
                result.append(path[:])
                return 
           
            #neighbors are the value of the graph at that index
            for neighbor in graph[index]:
                dfs(neighbor)
                if path:
                    path.pop()
                
        dfs(0)
        return result
                
        
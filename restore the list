class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        in_degree = [0] * len(adjacentPairs)
        ans = []
        visited = set()
        
        for edge in adjacentPairs:
            
            start,end = edge
            graph[start].append(end)
            graph[end].append(start)
            
            
        for value in graph:
            if len(graph[value]) == 1:
                start = value
                visited.add(start)
                break
                
    
                
        def dfs(node):
            
            ans.append(node)
            
            for adj in graph[node]:
                
                if not adj in visited:
                    visited.add(adj)
                    dfs(adj)
                    
        dfs(start)
        return ans
                
        
        
            
        
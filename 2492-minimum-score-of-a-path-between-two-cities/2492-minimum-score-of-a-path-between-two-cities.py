class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # find the minimum value after doing dfs starting at 1 let's just try it
        
        graph = defaultdict(list)
        visited = set()
        min_score = float('inf')
        for start,end,cost in roads:
            graph[start].append((end,cost))
            graph[end].append((start,cost))
            
        stack = [1]
        
        while stack:
            node = stack.pop()
            
            for child,cost in graph[node]:
                min_score = min(min_score,cost)
                if not child in visited:
                    visited.add(child)
                    stack.append(child)
        
        return min_score
              
            
        
        
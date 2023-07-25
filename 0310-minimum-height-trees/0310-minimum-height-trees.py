class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        if n <= 2:
            return [i for i in range(n)]
        
        graph = defaultdict(list)
        visited = set()
        in_degree = [0] * n
        queue = deque()
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
            
        for index in range(n):
            if in_degree[index] == 1:
                queue.append(index)
            
        while queue:
    
            level_size = len(queue)
            if level_size + len(visited) == n:
                break
            for _ in range(level_size):
                node = queue.popleft()
                visited.add(node)
                for child in graph[node]:
                    if not child in visited:
                        in_degree[child] -= 1

                        if in_degree[child] == 1:
                            queue.append(child)
                            
                    
            
        return queue
                        
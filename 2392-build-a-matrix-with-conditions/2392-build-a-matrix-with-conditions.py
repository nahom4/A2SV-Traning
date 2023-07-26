class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        k = k + 1
        def topological_sort(condition):
           
            graph = defaultdict(list)
            visited = set()
            queue = deque()
            ordered_list = []
            in_degree = [0] * (k)
            for u,v in condition:
                graph[u].append(v)
                in_degree[v] += 1
                
            for i in range(k):
                if i == 0:
                    continue
                if in_degree[i] == 0:
                    queue.append(i)
                    visited.add(i)
                    ordered_list.append(i)
                  
            while queue:
                
                node = queue.popleft()
                for child in graph[node]:
                    
                    if child in visited:
                        continue
                        
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queue.append(child)
                        visited.add(child)
                        ordered_list.append(child)
                
            return ordered_list
        
        virtical_sort = topological_sort(rowConditions)
        horizontal_sort = topological_sort(colConditions)

        k = k - 1
        if len(virtical_sort) < k or len(horizontal_sort) < k:
            return [] 
        
        grid = [[0] * k for _ in range(k)]
        
        virtical_sort_dict = {}
        for i in range(k):
            virtical_sort_dict[virtical_sort[i]] = i
            
        
        #fill horizontaly
        for i in range(k):
            grid[0][i] = horizontal_sort[i]
          
        #fill virtically
        for i in range(k):
            val = grid[0][i]
            row = virtical_sort_dict[val]
            grid[0][i] = 0
            grid[row][i] = val
            
        return grid
            
            
        
        
        
        
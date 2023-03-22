class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        dic = defaultdict(list)
        visited = set()
        tree_queue = deque()
        tree_queue.append(source)
        for edge in edges:
            first = edge[0]
            second = edge[1]
            dic[first].append(second)
            dic[second].append(first)
            
          # bfs solution
        while  tree_queue:
            
            val = tree_queue.popleft()
            if val == destination:
                return True
            for neighbor in dic[val]:
                if neighbor not in visited:
                    tree_queue.append(neighbor)
                    visited.add(neighbor)
        return False

            
# dfs
        #def dfs(n,source,destination):
#             visited.add(source)
#             if source == destination:
#                 return True
            
#             for neighbor in dic[source]:
                
#                 if neighbor not in visited and dfs(n,neighbor,destination):
#                     return True
            
#             return False
        
#         return dfs(n,source,destination)

       
      
        
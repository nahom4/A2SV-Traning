class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        #let's build the graph
        
        graph = defaultdict(list)
        in_degree = [0] * n
        ans = [set() for _ in range(n)]
        queue = deque()
        visited = set()
        
        for start,end in edges:
            
            graph[start].append(end)
            in_degree[end] += 1
     
        #collect only parent nodes
        for index in range(n):
            if in_degree[index] == 0:
                queue.append(index)
        
        while queue:
            
            node = queue.popleft()
            
            for child in graph[node]:
                #register the parent as a parent in the childs ancestor list
                #this is where the topological sort comes in
                ans[child].update(ans[node])
                ans[child].add(node)
                
                #let's fix the indegree of the child
                if not child in visited:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queue.append(child)
                        visited.add(node)
                    
        for index,ancestor in enumerate(ans):
            ancestor = sorted(list(ancestor))
            ans[index] = ancestor
            
        
        return ans
        
            
            
        
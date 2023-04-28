class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.result = 1
        graph = defaultdict(list)
        #let's form the graph
        for node in range(len(parent)):
            
            father = parent[node]
            if father == -1:
                continue
            graph[father].append(node)
        graph = dict(graph)    
        def dfs(node):
            
            if not node in graph:
              
                return 1
            
            children = graph[node]
            curr_max = 1
            lis = []
            for child in children:
                res = dfs(child)
                if s[child] != s[node]:
                    lis.append(res)
            
            lis.sort(reverse=True)
            
            if len(lis) >= 1:
                curr_max += lis[0]  
                
            if len(lis) >= 2:
                curr_max += lis[1]
                

            self.result = max(self.result,curr_max)
            return (lis[0] + 1) if lis else 1
        
        dfs(0)
        return self.result
                    
            
                    
                    
                
            
            
            
        
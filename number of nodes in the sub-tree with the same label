class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [1]*n
        #we need to build the graph
        graph = defaultdict(list)
        visited = set()
        for edge in edges:
            
            start,end = tuple(edge)
            graph[start].append(end)
            graph[end].append(start)
            
        
        graph = dict(graph)
        #dfs
        def add_to_collector(collector,count):
            
            for key in count:
                collector[key] += count[key]
            
        def dfs(node):
            label = labels[node]
            
         
            #we return a dictionary of count if node is not a key of the graph
            visited.add(node)
            if not node in graph:
                count = dict()
                count[label] = 1
                return count
            
            
            collecter = defaultdict(int)
            for child in graph[node]:
                if child not in visited:
                    res = dfs(child)
                    #add the res to the collecter
                    add_to_collector(collecter,res)
               
            
            collecter = dict(collecter)    
            ans[node] = collecter.get(label,0) + 1
            collecter[label] = collecter.get(label,0) + 1
            
            return collecter
        dfs(0)
        
        return ans
        
        
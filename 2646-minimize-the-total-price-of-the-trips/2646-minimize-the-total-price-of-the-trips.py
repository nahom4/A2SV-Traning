class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        ct = Counter()
        for edge in edges:
            start,end = edge
            graph[start].append(end)
            graph[end].append(start)
    
        res = []
        def dfs(node, target,ans):
            visited.add(node)  
            ans.append(node)
            nonlocal res
            if node == target:
                res = list(ans)
                
            for child in graph[node]:
                if child not in visited:
                    dfs(child,target,ans)
                    ans.pop()
                      
        for trip in trips:
            visited = set()
            res = []
            start,end = trip
            dfs(start,end,[])
            for value in res:
                ct[value] += 1
        
        @cache
        def dp(node,parent):
    
            ans = [ct[node] * (price[node]),ct[node] * (price[node]) // 2] # nothalf, half
            for child in graph[node]:
                if child == parent:
                    continue
                #it is a pick or leave problem 1 idicates option 0 
                notHalf,half = dp(child,node)
                ans[0] += min(notHalf,half)
                ans[1] += notHalf
 
            return ans
        return min(dp(0,None))
                    
            
            
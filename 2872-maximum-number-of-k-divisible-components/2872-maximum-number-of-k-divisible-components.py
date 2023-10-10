class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        
        #let's follow a greedy approach
        #each node returns their value if the sum of nodes so far is divisible 
        #by k this can be cut but only if totol - k is divisible by k
        #we need to deduct from total the current sum and increament count
        
        graph = defaultdict(list)
        
        for left,right in edges:
            graph[left].append(right)
            graph[right].append(left)
            
            
        total = sum(values)
        visited = set()
        ct = 0
        def dfs(node):
            nonlocal ct
            nonlocal total
            if node == None:
                return 0
            
            if node in visited:
                return 0
            
            visited.add(node)
            curr = 0
            for child in graph[node]:
                curr += dfs(child)
                
            curr += values[node]
            if curr % k == 0 and (total - curr) % k == 0:
                total -= curr
                ct += 1
                return 0
            
            return curr
        
        dfs(0)
        return ct
        
        
        

                
        
        
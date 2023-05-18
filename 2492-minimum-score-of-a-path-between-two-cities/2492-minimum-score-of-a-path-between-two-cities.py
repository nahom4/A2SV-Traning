class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # find the minimum value after doing dfs starting at 1 let's just try it
        
        rep = {i : i for i in range(1,n + 1)}
        size = { i : 1  for i in range(1,n + 1)}
        minima = { i : float('inf') for i in range( 1,n + 1)}
        
        def find(node):
            
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(first,second,cost):
            
            firstParent = find(first)
            secondParent = find(second)
            
            if size[firstParent] < size[secondParent]:
                firstParent,secondParent = secondParent,firstParent
                
                
            minima[firstParent] = min(minima[firstParent],minima[secondParent],cost)
            
            if firstParent != secondParent:
                rep[secondParent] = firstParent
        
        
        for connection in roads:
            
            first,second,cost = connection
            union(first,second,cost)
        
        repOne = find(1)
        return minima[repOne]
              
            
        
        
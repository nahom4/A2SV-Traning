class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges) 
        rep = {i : i for i in range(1,n + 1)}
        size = {i : 1 for i in range(1,n + 1)}
        last_edge = []
        
        def find(node):
            
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(first,second):
            
            firstParent = find(first)
            secondParent = find(second)
          
            if firstParent == secondParent:
            
                last_edge.append([first,second])
              
            if size[firstParent] < size[secondParent]:
                firstParent,secondParent = secondParent,firstParent
                
            size[firstParent] += size[secondParent]
            rep[secondParent] = firstParent
           
            
        for first,second in edges:
            
            union(first ,second)
            
        return last_edge[-1]
            
        
        
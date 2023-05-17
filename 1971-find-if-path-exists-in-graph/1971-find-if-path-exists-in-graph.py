class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        rep = {i : i for i in range(n)}
        store = [1] * n
        
        # use quick union
        def findRep(node):
            parent = node
            while parent != rep[parent]:
                
                parent = rep[parent]
                
            #let's do here path comprehension
            while node != rep[node]:
                oldParent = rep[node]
                rep[node] = parent
                node = oldParent
            
            return parent
        
        def union(first, second):
            
            repFirst = findRep(first)

            repSecond = findRep(second)
              
            lnFirst = store[repFirst]
            lnSecond = store[repSecond]
            
            if lnFirst > lnSecond:
                rep[repSecond] = repFirst
                store[repFirst] += store[repSecond]
                
            else:
                rep[repFirst] = repSecond
                store[repSecond] += store[repFirst]
                       
        #build the grouping
        for first,second in edges:
            union(first,second)
            
        return findRep(source) == findRep(destination)
                
            
        
       

       
      
        
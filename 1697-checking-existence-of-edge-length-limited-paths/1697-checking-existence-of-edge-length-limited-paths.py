class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        rep = {i : i for i in range(n)} 
        size = {i : 1 for i in range(n)}
        Q = len(queries)
        def find(node):
            
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(first,second):
            
            firstParent = find(first)
            secondParent = find(second)
            
            if size[firstParent] < size[secondParent]:
                firstParent,secondParent = secondParent,firstParent
                            
            if firstParent != secondParent:
                rep[secondParent] = firstParent
                
        edges = defaultdict(list)
        querys = defaultdict(list)
        
        for u,v,distance in edgeList:
            edges[distance].append((u,v))
            
        for index,(u,v,distance) in enumerate(queries):
            querys[distance].append((u,v,index))
        
        distances = list(set(list(querys.keys()) + list(edges.keys())))
        distances.sort()
        answer = [True] * Q
        for distance in distances:
            
            if len(querys[distance]) > 0:
                for u,v,index in querys[distance]:
                    answer[index] = find(u) == find(v)
            
            if len(edges[distance]) > 0:
                for u,v in edges[distance]:
                    union(u,v)
                    
        return answer
                    
            
        
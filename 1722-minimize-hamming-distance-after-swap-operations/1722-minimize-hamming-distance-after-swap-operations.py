class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        rep = {i : i for i in range(n)}
        size = {i : 1 for i in range(n)}
        def find(node):
            
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(node1,node2):
            first_parent,second_parent = find(node1),find(node2)
            
            if first_parent == second_parent:
                return 
            
            if size[first_parent] < size[second_parent]:
                first_parent,second_parent = second_parent,first_parent
                
            size[first_parent] += size[second_parent]
            rep[second_parent] = first_parent
        
        for swap in allowedSwaps:
            union(swap[0],swap[1])
            
        dic = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            parent = find(i)
            dic[parent][source[i]] += 1
        
        hamming_distance = 0
        for i in range(n):
            char = target[i]
            parent = find(i)
            if dic[parent][char] > 0:
                dic[parent][char] -= 1
                
                    
            else:
                
                hamming_distance += 1
                
        return hamming_distance
                

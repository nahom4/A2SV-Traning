class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        rep = {(s[index],index): (s[index],index) for index in range(len(s))}
        size = {(s[index],index): 1 for index in range(len(s))}
    
        def find(node):
            
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            
            rep[node] = parent
            
            return parent
        
        def union(node1,node2):
  
            first_parent = find(node1)
            second_parent = find(node2)
            
            if first_parent == second_parent:
                return
            
            if size[first_parent] < size[second_parent]:
                first_parent,second_parent = second_parent,first_parent
                
            size[first_parent] += size[second_parent]
            rep[second_parent] = first_parent
            
        
        for pair in pairs:
            union((s[pair[0]],pair[0]),(s[pair[1]],pair[1]))
        
        new_rep = defaultdict(list)
        for index in range(len(s)):
            new_rep[find((s[index],index))].append(s[index])
            
        for key in new_rep:
            new_rep[key].sort(reverse=True)
            
        res = ""
        for index in range(len(s)):
            res += new_rep[find((s[index],index))].pop()
        
        return res
            
        
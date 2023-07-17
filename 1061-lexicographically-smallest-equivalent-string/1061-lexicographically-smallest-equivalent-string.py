class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        rep = {letter : letter for letter in (string.ascii_lowercase)}
        
        size = {letter : 1 for letter in (string.ascii_lowercase)}
        
        
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
            
        for char1,char2 in zip(s1,s2):
            union(char1,char2)
            
        char_dict = defaultdict(list)
        for char in string.ascii_lowercase:
            parent = find(char)
            if not char_dict[parent]:
                char_dict[parent].append(char)
                
        answer = []
        
        for char in baseStr:
            parent = find(char)
            answer.append(char_dict[parent][0])
            
        return "".join(answer)
        
                
                
                
        
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        equal = []
        not_equal = []
        
        for equation in equations:
            if '!' in equation:
                not_equal.append(equation)
            else:
                equal.append(equation)
       
    
        #group the equations based on the equal list then check if it is valid with 
        #the not_equal list
        
        res = {letter: letter for letter in string.ascii_lowercase}
        size = {letter: 1 for letter in string.ascii_lowercase}
        
        def find(node):
            
            if node == res[node]:
                return node
            
            parent = find(res[node])
            res[node] = parent
            
            return parent
        
        def union(node1,node2):
            
            first_parent = find(node1)
            second_parent = find(node2)
            
            if first_parent == second_parent:
                return
            
            if size[first_parent] < size[second_parent]:
                first_parent,second_parent = second_parent,first_parent
                
            size[first_parent] += size[second_parent]
            res[second_parent] = first_parent
            
        for equation in equal:
            union(equation[0],equation[-1])
            
        for equation in not_equal:
            if find(equation[0]) == find(equation[-1]):
                return False
        return True
            
            
        
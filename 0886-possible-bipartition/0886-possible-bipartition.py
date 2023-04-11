class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        #form an adjecency list
        graph = defaultdict(list)
        one = set()
        two = set()
        for edge in dislikes:
            person,enemy = edge
            graph[person].append(enemy)
            
       #dfs

        def dfs(node,group):
            
            if group:
                if node in two:
                    return False
                if node not in one:
                    one.add(node)
                else:
                    return True
            else:
                if node in one:
                    return False
                if node not in two:
                    two.add(node)
                else:
                    return True
                
            #iterate over the enemies
            if node not in graph:
                return True
            
            for enemy in graph[node]:
                valid = dfs(enemy,not group)
                if not valid:
                    return False
                
            return True
      
        #Ther might be components
       
        for person in graph:
            if not person in one and not person in two:
                one,two = set(),set()
                valid = dfs(person,True)
                if not valid:
                    return False
        return True
        
                
            
        
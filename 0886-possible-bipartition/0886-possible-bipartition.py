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

        def dfs(node,my_group,enemy_group):
            
            if node in my_group:
                return True
            if node in enemy_group:
                return False
            my_group.add(node)
            
            #iterate over the enemies
            if node not in graph:
                return True
            
            for enemy in graph[node]:
                valid = dfs(enemy,enemy_group,my_group)
                if not valid:
                    return False
                
            return True
      
        #Ther might be components
       
        for person in graph:
            if not person in one and not person in two:
                one,two = set(),set()
                valid = dfs(person,one,two)
                if not valid:
                    return False
        return True
        
                
            
        
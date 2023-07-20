class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        friend_rep = {i : i for i in range(n)}
        friends = {i : {i} for i in range(n)}
        enemy_rep = {i : i for i in range(n)}
        enemies = {i : [] for i in range(n)}
        
        def find(node,rep):
            
            if rep[node] == node:
                return node
            
            parent = find(rep[node],rep)
            rep[node] = parent
            
            return parent
        
        def union(node1,node2,rep):
            first_parent,second_parent = find(node1,rep),find(node2,rep)
            
            if first_parent == second_parent:
                return 
            
            if len(friends[first_parent]) < len(friends[second_parent]):
                first_parent,second_parent = second_parent,first_parent
                
            friends[first_parent].update(friends[second_parent])
            enemies[first_parent].extend(enemies[second_parent])
            rep[second_parent] = first_parent
                
        for pair in restrictions:
            first,second = pair[0],pair[1]
            enemies[first].append(second)
            enemies[second].append(first)
        
        answer = []
        for pair in requests:
            valid = True
            first,second = pair[0],pair[1]
            parent = find(first,enemy_rep) # find the enemy group rep
            for person in enemies[parent]:
                f_parent = find(person,friend_rep) # find the freind group rep
                if second in friends[f_parent]:
                    valid = False
            if valid:
                union(first,second,friend_rep)
                union(first,second,enemy_rep)
            answer.append(valid)
            
        return answer
            
        
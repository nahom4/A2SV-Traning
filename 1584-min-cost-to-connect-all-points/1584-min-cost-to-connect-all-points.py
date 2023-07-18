class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #maybe a brute force approach might be possible calculate the distance
        #between each point and sort them then connect 
        
        def manhattan_distance(i,j):
            x1,y1 = points[i]
            x2,y2 = points[j]
            return abs(x2 - x1) + abs(y2 - y1)
        n = len(points) 
        rep = {i : i for i in range(n)}
        size = {i : 1 for i in range(n)}
        total = 0
        def find(node):
            parent = node
            while rep[parent] != parent:
                parent = rep[parent]
                
            while rep[node] != node:
                temp = rep[node]
                rep[node] = parent
                node = temp
            
            return parent
        
        def union(node1,node2,cost):
            nonlocal total
            first_parent,second_parent = find(node1),find(node2)
            
            if first_parent == second_parent:
                return
            
            if size[first_parent] < size[second_parent]:
                first_parent,second_parent = second_parent,first_parent
            
            size[first_parent] += second_parent
            rep[second_parent] = first_parent
            
            total += cost
           
        distance = []
        for i in range(len(points)):
            for j in range(i + 1,len(points)):
                distance.append([manhattan_distance(i,j),i,j])
                
        distance.sort()
        for val in distance:
            cost,node1,node2 = val
            union(node1,node2,cost)
            
        return total
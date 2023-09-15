class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = list(map(tuple,points))
        rep = {point : point for point in points}
        rank = {point : 1 for point in points}
        
        def find(node):
            
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            return parent
        
        
        def union(firstNode,secondNode):
            firstNodeParent,secondNodeParent = find(firstNode),find(secondNode)
            
            if firstNodeParent == secondNodeParent:
                return False
            
            if rank[firstNodeParent] < rank[secondNodeParent]:
                firstNodeParent,secondNodeParent = secondNodeParent,firstNodeParent
                
            rep[secondNodeParent] = firstNodeParent
            rank[firstNodeParent] += rank[secondNodeParent]
            return True
            
        def manhattanDistance(pointA,pointB):
            xA,yA = pointA
            xB,yB = pointB
            
            return abs(xA - xB) + abs(yA - yB)
            
        pairs = []
        N = len(points)
        for i in range(N):
            for j in range(N):
                if i == j: 
                    continue
                pairs.append((manhattanDistance(points[i],points[j]),points[i],points[j]))
                
        pairs.sort()
        minCost = 0
        for distance,pairA,pairB in pairs:
            if union(pairA,pairB):
                minCost += distance
                
                
        return minCost
                
            
            
        
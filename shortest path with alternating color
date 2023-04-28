class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        red_dict = defaultdict(list)
        blue_dict = defaultdict(list)
        visited = set()
        ans = [2 * n] * n
        
        for red_edge in redEdges:
          
            start,end = red_edge
            red_dict[start].append(end)
            
        for blue_edge in blueEdges:
            
            start,end = blue_edge
            blue_dict[start].append(end)
         
     
        queue = deque()
        ans[0] = 0
        if red_dict[0]:
            for i in range(len(red_dict[0])):
                queue.append((red_dict[0][i],1,1))
        if blue_dict[0]:
            for i in range(len(blue_dict[0])):
                queue.append((blue_dict[0][i],0,1))
            
        while queue:
            
            node,color,level = queue.popleft()
            ans[node] = min(ans[node],level)
            store = red_dict if color == 0 else blue_dict
            nxt_color = 1 - color
            for child in store[node]:
                
                if not (child,nxt_color) in visited:
                    visited.add((child,nxt_color))
                    queue.append((child,nxt_color,level + 1))
     
        ans = map(lambda value: -1 if value == 2 * n else value,ans)
        return ans
                    
        
        
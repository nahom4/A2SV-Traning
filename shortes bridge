class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        #let's use dfs to find on the islands and then do bfs to find the shortest distance
        #between this island and the next
        
        
        queue = deque()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def in_bound(pos):
            row,col = pos
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(pos):
            row,col = pos
            visited.add((row,col))
            add = False
            for x,y in direction:
                
                nxt_row,nxt_col = (row + x,col + y)
                if in_bound((nxt_row,nxt_col)) and not (nxt_row,nxt_col) in visited:
                   
                    if grid[nxt_row][nxt_col] == 1:
                        dfs((nxt_row,nxt_col))
                        
                    else:
                        add = True
                        
            if add:
                queue.append((row,col,0))
                
        for index, level in enumerate(grid):
            
            if 1 in level:
                
                row = index
                col = level.index(1)
                break
                
        dfs((row,col))
        #now we have identified one island let's do bfs find the nearest 1 in the grid
        while queue:
            row,col,level = queue.popleft()
             
            for x,y in direction:
                
                nxt_row ,nxt_col = (x + row,y + col)
                if in_bound((nxt_row,nxt_col)) and not (nxt_row,nxt_col) in visited:
                    
                    if grid[nxt_row][nxt_col] == 1:
                        return level 
                    
                    queue.append((nxt_row,nxt_col,level + 1))
                    visited.add((nxt_row,nxt_col))
            
       
        return -1
                
        
        
        
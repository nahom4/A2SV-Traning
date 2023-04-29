class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        queue = deque()
        queue.append((entrance[0],entrance[1],0))
        res = -1
        visited = set()
        def in_bound(pos):
            row,col = pos
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            
            row,col,level = queue.popleft()
            
            if (row,col) != (entrance[0],entrance[1]) and (row == 0 or col == 0 or  row == len(maze) - 1 or col == len(maze[0]) - 1):
                res = level
                break
                
                
            for x,y in direction:
                nxt_x = x + row
                nxt_y = y + col
                pos = (nxt_x,nxt_y)
                
                if in_bound(pos) and not pos in visited and  maze[nxt_x][nxt_y] == '.':
                    visited.add((nxt_x,nxt_y))
                    queue.append((nxt_x,nxt_y,level + 1))
                    
        return res
                    
                    
                
            
        
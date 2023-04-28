class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #the level indicates the time
        queue = deque()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def in_bound(pos):
            row,col = pos
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
       
        time = 0
        while queue:
            
            size = len(queue)
            for _ in range(size):
                
                r,c = queue.popleft()
                for x_drc,y_drc in direction:
                    row = r + x_drc
                    col = c + y_drc
                    if in_bound((row,col)) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row,col))
                    
            time += 1
            
        if any(1 in sub_list for sub_list in grid):
            return -1 
        if any(2 in sub_list for sub_list in grid):
            return time - 1
        return 0
               
                
                
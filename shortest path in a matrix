class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        queue = deque()
        res = -1
        visited = set((0,0))
        target = (len(grid) - 1, len(grid[0]) - 1)
        if grid[0][0] == 1:
            return -1
        
        queue.append((0,0,1))
        
        def in_bound(pos):
            row,col = pos
            
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        while queue:
            
            row,col,level = queue.popleft()
            
            if (row,col) == target:
                res = level
                break
          
            visited.add((0,0))
                
            #move in the 8 directions
            
            for r in range(row - 1,row + 2):
                for c in range(col - 1,col + 2):
                                        
                    if (r,c) not in visited and in_bound((r,c)) and grid[r][c] == 0:
                        queue.append((r,c,level + 1))
                        visited.add((r,c))
                        
                        
        return res
            
        
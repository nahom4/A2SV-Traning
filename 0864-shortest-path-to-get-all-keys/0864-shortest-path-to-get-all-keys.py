class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
        #There different possible pahths we could take 
        #while travelling I need to collect the key I find along the way
        # The trick is i store both the postion and my set of keys in the visited set
        
        visited = set()
        queue = deque()
        target = set()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        
        [target.add(char.lower()) if char.isalpha() else None for lis in grid for char in lis]
        
        def can_enter(state):
           
            row,col,keys = state 
            if '@' == grid[row][col]:
                
                return True
            if grid[row][col].isalpha():
                if  grid[row][col].isupper():
                    if not grid[row][col].lower() in keys:
                        return False
            else:
               
                return grid[row][col] == '.'
            
            return True
                            

        def in_bound(pos):
            row,col = pos

            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        row = 0
        col = 0
        for index, lis in enumerate(grid):
            if '@' in lis:
                col = lis.index('@')
                row = index
        
    
            
        queue.append((row,col,set()))
        visited.add((row,col,tuple))
        dic = defaultdict(tuple)
            
        level = 0
        while queue:
            level += 1
            length = len(queue)
            for _ in range(length):
                row,col,keys = queue.popleft()
              
                #collect a key if it exists
                if grid[row][col].isalpha():
                    keys.add(grid[row][col].lower())
                    
                if keys == target:
                    return level - 1
                    
                #add the neibhors
                for x,y in direction:
                    nxt_x, nxt_y = x + row,y + col
                        
                    if in_bound((nxt_x,nxt_y)) and not (nxt_x,nxt_y,tuple(keys)) in visited and can_enter((nxt_x,nxt_y,keys)):
                        dic[(nxt_x,nxt_y)] = (row,col)
                        visited.add((nxt_x,nxt_y,tuple(keys)))
                        queue.append((nxt_x,nxt_y,set(keys)))
            
                
        
        return -1
            
        
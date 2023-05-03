class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        queue = deque()
        queue.append((board,0))
        target = [[1,2,3],[4,5,0]]
        visited = set()
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def find_zero(curr):
            row = 0
            col = 0
            
            if 0 in curr[0]:
                col = curr[0].index(0)
            else:
                row = 1
                col = curr[1].index(0)
                
            return (row,col)
        
        def change(curr):
            
            return (tuple(curr[0]),tuple(curr[1]))
          
        def in_bound(pos):
            row,col = pos
            
            return 0 <= row < 2 and 0 <= col < 3
        
        while queue:
        
            curr,level = queue.popleft()
            row,col = find_zero(curr)
            
            if curr == target:
                
                return level
            
            #get the other states
            
            for x,y in direction:
                
                if in_bound((x + row,y + col)):
                    
                    nxt = list((list(curr[0]),list(curr[1])))
                    nxt[row][col],nxt[row + x][y + col] = nxt[row + x][y + col],nxt[row][col]
                    changed = change(nxt)
                    
                
                    if not changed in visited:
                        queue.append((nxt,level + 1))
                        visited.add(changed)
                        
        return -1
            
            
        
        
        
        
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #The problem is like the roten oranges problem the only difference here is the
        # the 0 is the rotten oranges and 1 is the fresh ones
        def in_bound(pos):
            row,col = pos
            
            return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        #perform bfs for each element
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque()
        
        ans = [[0]*len(mat[0]) for _ in range(len(mat))]
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                
                if mat[row][col] == 0:
                    queue.append((row,col,0))
                  
        while queue:
            row,col,level = queue.popleft()
            
            for x_drc,y_drc in direction:
                nxt_x,nxt_y = (x_drc + row,y_drc + col)
                if in_bound((nxt_x,nxt_y)) and mat[nxt_x][nxt_y] == 1:
                    mat[nxt_x][nxt_y] = 0
                    ans[nxt_x][nxt_y] = level + 1
                    queue.append((nxt_x,nxt_y,level + 1))
                    
        return ans
                    
                    
            
                   
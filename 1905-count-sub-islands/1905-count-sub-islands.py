class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        #need to find islands
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        def dfs(pos):
            
            row,col = pos
           
            if 0 <= row < len(grid2)  and 0 <= col < len(grid2[0]) and  grid2[row][col] == 1:
                pass
            else:
                return 
            
            if grid1[row][col] == 0:
                self.is_sub = False
            
    
            grid2[row][col] = 0
            
            for drc in direction:
                dfs((drc[0] + pos[0],drc[1] + pos[1]))
                
               
                
                         
                
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                
                if grid2[row][col] == 1:
                    
                    self.is_sub = True
                    
                    dfs((row,col))
                
                    if self.is_sub:
                        count += 1
                        
                    #add temp1 to visited
                    
                    
                    
        return count
                    
                    
                
                
            
        
        
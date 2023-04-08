class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        visited = set()
        def in_bound(pos):
            row,col = pos
            return (row >= 0 and row < len(image) and col >= 0 and col < len(image[0]))
        def dfs(pos,color,prev):
            
            row,col = pos
            image[row][col] = color
            visited.add(pos)
            
            if in_bound((row - 1,col)) and image[row - 1][col] == prev and not (row - 1,col) in visited:
                dfs((row - 1,col),color,prev)
            if in_bound((row + 1,col)) and image[row + 1][col] == prev and not (row + 1,col) in visited:
                dfs((row + 1,col),color,prev)
            if in_bound((row,col - 1)) and image[row][col -1] == prev and not (row,col - 1) in visited:
                dfs((row,col - 1),color,prev)
            if in_bound((row,col + 1)) and image[row][col + 1] == prev and not (row,col + 1) in visited:
                dfs((row,col + 1),color,prev)
                
        dfs((sr,sc),color,image[sr][sc])
        return image
                                                      
            
            
            
            
            
        
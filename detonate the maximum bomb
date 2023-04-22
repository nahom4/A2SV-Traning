class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        final = 0
        visited = set()
        def in_range(curr,nxt):
           
            x,y,r = tuple(curr)
            
            nxt_x,nxt_y,_ = tuple(nxt)
         
            # x2 - x1 ** 2 + y2 - y1 ** 2 and then square root the whole thing
            distance = ((nxt_x - x) ** 2 + (nxt_y - y) ** 2) ** 0.5
        
            return distance <= r
        
        def dfs(bomb,index):
            
            if exploded[index] == 1:
                return
            
            exploded[index] = 1
            visited.add(index)
            self.count += 1
            
            for i,nxt in enumerate(bombs):
                
                if in_range(bomb,nxt) and exploded[i] != 1:
                    
                    dfs(nxt,i)
                    
            
        for index, bomb in enumerate(bombs):
            self.count = 0
            exploded = [0] * len(bombs)
            if index not in visited:
                dfs(bomb,index)
            
                final = max(final,self.count)
            
        return final
            
            
            
            
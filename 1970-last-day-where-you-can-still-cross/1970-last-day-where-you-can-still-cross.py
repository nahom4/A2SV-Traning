class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        direction = [(1,0),(-1,0),(0,1),(0,-1)] 
        start = [[0] * col for _ in range(row)]
        #flood the area
        
        for cell in cells:
            rw,cl = cell
            start[rw - 1][cl - 1] = 1
           
        rep = {}
        size =  {}
        group =  {}
        for i in range(row):
            for j in range(col):
                
                rep[(i,j)] = (i,j)
                size[(i,j)] = 1
                if i == 0:
                    group[(i,j)] = 1 # top group
                elif i == row - 1:
                    group[(i,j)] = -1 # bottom group
                    
                else:
                    group[(i,j)] = 0 # middle group
               
        def valid(pos):
            rw,cl = pos
            
            return 0 <= rw < row and 0 <= cl < col
        def is_water(pos):
            row,col = pos
            return start[row][col]
        def change_group(first_parent,second_parent):
            first_group,second_group = group[first_parent],group[second_parent]
            if first_group + second_group == 0:
                if first_group == 1 or second_group == 1:
                    return True
            
            if first_group == 0:
                group[first_parent] = second_group
                
            
                    
        def find(node):
            parent = node
            while rep[parent] != parent:
                parent = rep[parent]
                
            while rep[node] != node:
                temp = rep[node]
                rep[node] = parent
                node = temp
            
            return parent
        
        def union(node1,node2):
         
            first_parent,second_parent = find(node1),find(node2)
          
            if is_water(node1) or is_water(node2):
                return
            
            if first_parent == second_parent:
                return
            
            if size[first_parent] < size[second_parent]:
                first_parent,second_parent = second_parent,first_parent
            
            size[first_parent] += size[second_parent]
            rep[second_parent] = first_parent
            
            # change the group
            if change_group(first_parent,second_parent):
                
                return True
        
        result = len(cells)
        for i in range(row):
            for j in range(col):
                for x,y in direction:
                    if valid((i + x,j + y)):
                        if union((i,j),(i + x,j + y)):
                            return result
        result -= 1
        for i in range(len(cells) - 1,-1,-1):
            rw,cl = cells[i]
            rw -= 1
            cl -= 1
            start[rw][cl] = 0
            for x,y in direction:
                    if valid((rw + x,cl + y)):
                        if union((rw,cl),(rw + x,cl + y)):
                            return result
                    
            result -= 1
            
                    
                
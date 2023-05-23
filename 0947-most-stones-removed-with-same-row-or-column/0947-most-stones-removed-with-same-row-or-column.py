class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        #let's process the stones
        
        rows = defaultdict(list)
        column = defaultdict(list)
        
        stones = [tuple(stone) for stone in stones]
        for stone in stones:
            row,col = stone
            rows[row].append(stone)
            column[col].append(stone)
        
        rep = {stone : stone for stone in stones}
        size = {stone : 1 for stone in stones}
    
        def find(node):
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(first,second):
          
            firstParent = find(first)
            secondParent = find(second)
            
            if firstParent == secondParent:
                return
            if size[firstParent] < size[secondParent]:
                firstParent,secondParent = secondParent,firstParent
                
            size[firstParent] += size[secondParent]
            rep[secondParent] = firstParent
            size[secondParent] = 0
            
        
        for stone in stones:
            
            for neighbour in rows[stone[0]]:
                
                union(stone,neighbour)
            for neighbour in column[stone[1]]:
                union(stone,neighbour)
                
        res = list(size.values())
        total = 0
        for value in res:
            if value == 0:
                continue
            total += value - 1
       
        return total
        
       
            
            
        
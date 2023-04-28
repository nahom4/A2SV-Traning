class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        # at any point we can turn one of the four wheels either closckwise or anti clockwise
        
        queue = deque()
        queue.append(('0000',0))
        visited = set()
        visited.add('0000')
        res = -1 
        deadends = set(deadends)
        
        if '0000' in deadends:
            return -1 
        
        while queue:
            
            node,level = queue.popleft()
            if node == target:
                res = level
                break
                
            
            
            for i in range(4):
                lis = list(node)
                value = int(lis[i])
                
                #clockwise
                lis[i] = (value + 1) % 10
                clw = ''.join(list(map(str,lis)))
                if clw not in visited and clw not in deadends:
                    queue.append((clw,level + 1))
                    visited.add(clw)
                
                #counterclockwise
                lis[i] = (value - 1) % 10
                cclw = ''.join(list(map(str,lis)))
                if cclw not in visited and cclw not in deadends:
                    queue.append((cclw,level + 1))
                    visited.add(cclw)
        
                    
        return res
                
        
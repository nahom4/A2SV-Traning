class Solution:
    def racecar(self, target: int) -> int:
        
        #we have two possbile operations A AND R so we alternate between the two and build
        #a tree which we will traverse with bfs to find the shortest distance to the target
        
        queue = deque()
        queue.append((0,1,0))
        visited = set()
        
        while queue:
            
            pos,speed,level = queue.popleft()
            
            if pos == target:
                res = level
                break
            
            #two events could take place either accelerate or reverse
            a_speed = speed * 2
            a_pos = pos + speed
            
            if not (a_pos,a_speed) in visited:
                queue.append((a_pos,a_speed,level + 1))
                visited.add((a_pos,a_speed))
            
            if speed > 0:
                r_speed = -1
                r_pos = pos
                if not (r_pos,r_speed) in visited:
                    queue.append((r_pos,r_speed,level + 1))
                    visited.add((r_pos,r_speed))
            else:
                r_speed = 1
                r_pos = pos
                if not (r_pos,r_speed) in visited:
                    queue.append((r_pos,r_speed,level + 1))
                    visited.add((r_pos,r_speed))
                
            
        return res
                
        
            
            
        
        
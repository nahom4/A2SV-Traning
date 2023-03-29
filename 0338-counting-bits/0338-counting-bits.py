class Solution:
    def countBits(self, n: int) -> List[int]:
        
        memory = dict()
        memory[0] = 0
        result = []
        
        for value in range(n + 1):
            count = 0
            if value & 1 == 1:
                count += 1
                
            nxt = value >> 1
            count += memory[nxt]
            memory[value] = count
            result.append(count)
            
        return result
            
        
            
        
        
                
                
                
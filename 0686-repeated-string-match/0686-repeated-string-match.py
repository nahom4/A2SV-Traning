class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        
        N = len(b)
        i = 1
        M = len(a)
        j = 0
        lps = [0] * N
        
        while i < N:
            if b[i] == b[j]:
                lps[i] = j + 1
                i += 1
                j += 1
                
            elif j == 0:
                i += 1
                
            else:
                j = lps[j - 1]
                
        i,j = 0,0
        M = len(a) #dup
        N = len(b) # serach
        
        state = set()
        rep = 0 
        while True:
            idx = i % M
            
            if (idx, j) in state:
                return -1
        
            state.add((idx,j))
            if idx == 0:
                rep += 1
                
                
            if a[idx] == b[j]:
                i += 1
                j += 1
                
            elif j == 0:
                i += 1
            
            else:
                j = lps[j - 1]
                
            if j ==  N:
                return rep 
                
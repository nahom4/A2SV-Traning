class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        prefix_sum = [0]*size
        
        for query in shifts:
            start,end,direction = tuple(query)
            
            
            
            if direction == 0:
                prefix_sum[start] -= 1
                if len(prefix_sum) > end + 1:
                    prefix_sum[end+1] += 1
            else:
                prefix_sum[start] += 1
                if len(prefix_sum) > end + 1:
                    prefix_sum[end+1] -= 1
        print(prefix_sum)
                    
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i]  + prefix_sum[i-1]
            
        result = ""
            
        for i in range(len(prefix_sum)):
            
            value = (ord(s[i]) - 97 + prefix_sum[i])%26 + 97
            result += chr(value)
            
        return result
            
                
     
                
            
                
        
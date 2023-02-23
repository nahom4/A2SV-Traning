from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #add
        #validate
        #remove
        #update
        
    
        n = len(s)
        
        left = 0
        dic = Counter()
        
        
        max_length = 0
        
        #calculate max of a dictionary
        
        for right in range(n):
            
            dic[s[right]] += 1
            
            while (k -((right - left + 1) - max(dic.values()))) < 0:
              
                dic[s[left]] -= 1
                        
                left += 1
            
            max_length = max(max_length,right - left + 1)
        
        return max_length
            
            
                
                
            
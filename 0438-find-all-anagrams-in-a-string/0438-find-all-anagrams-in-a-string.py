class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        n = len(s)
        k = len(p)
        left = 0 
        outer_dic = Counter(p)
        
        inner_dic = Counter()
        result = []
        
        
        for right in range(n):
            inner_dic[s[right]] += 1
            
            if right - left + 1 == k:
             
                if outer_dic == inner_dic:
                    result.append(left)
                    
                inner_dic[s[left]] -= 1
                left += 1
                
        return result
                    
            
                    
                    
                
        
        
        
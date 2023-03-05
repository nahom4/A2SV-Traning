class Solution:
    def balancedString(self, s: str) -> int:
        
        left = 0
        n = len(s)
        expected = n//4
        count = Counter(s)
        temp = Counter()
        result = n
 
        #let's preprocess and identify the letters with count greater than expected
        target = []
        for key in count:
            if count[key] > expected:
                target.append(key)
      
        def validate():
            for key in temp:
                if temp[key] >= count[key] - expected:
                    continue
                else:
                    return False
            return True
        
        if not target:#edge case
            return 0
        
        for x in target:#initialize with a zero
            temp[x] = 0
            
        for right in range(n):
            #add
            if s[right] in target:
                temp[s[right]] += 1
            
           
            #validate
            while left <= right and validate():
                result = min(result,right - left + 1)
                
                if s[left] in target:
                    temp[s[left]] -= 1
                left += 1
                
            
        return result
                
                
            
            
            
        
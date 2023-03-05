class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count = Counter(t)
        left = 0
        temp = Counter()
        n = len(s)
        result = math.inf
        start = 0
        end = 0
        flag = False
        
        def validate():
            for key in count:
                if count[key] <= temp.get(key,0):
                    continue
                else:
                    return False
            return True
        
        for right in range(n):
            
            temp[s[right]] += 1
          
            
            while left <= right and validate():
                flag = True
                if right - left + 1 < result:
                    start = left
                    end = right
                    result = right - left + 1
                temp[s[left]] -= 1
                if temp[s[left]] == 0:
                    del(temp[s[left]])
                left += 1
              
        if flag:
            return s[start:end+1]
        else:
            return ''
                
            
        
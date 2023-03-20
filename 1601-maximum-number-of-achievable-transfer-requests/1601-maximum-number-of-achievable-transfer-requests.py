from collections import defaultdict
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        curr = []
        max_length = 0
        
        def check(lis):
            dic = defaultdict(int)
           
            for x in lis:
                dic[x[0]] += 1
                dic[x[1]] -= 1
                
            for key in dic:
                if dic[key] == 0:
                    continue
                else:
                    return False
            return True
          
         
        def backtrack(index):
            nonlocal max_length
            if curr and check(curr):
                
                max_length = max(max_length,len(curr))
            
            if index >= len(requests):
                return
            
            curr.append(requests[index])
            backtrack(index + 1)
            curr.pop()
            backtrack(index + 1)
            
        backtrack(0)
        return max_length
      
      
                
            
            
        
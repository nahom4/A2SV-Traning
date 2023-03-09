class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.mn = sum(cookies)
        bucket = [0]*k
        def distribute(index):
            
            if index == len(cookies):
               
                self.mn = min(self.mn,max(bucket))
                return
                
            if max(bucket) > self.mn:
                return
            
            for i in range(k):
               
                bucket[i] += cookies[index]
                
                distribute(index + 1)
                bucket[i] -= cookies[index]
                if bucket[i] == 0: return
                
                
        distribute(0)
        return self.mn
                
                
                
                
                
                
        
        
        
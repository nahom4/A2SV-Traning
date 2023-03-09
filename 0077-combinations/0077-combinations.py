class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        array =  [i for i in range(1,n + 1)]
        ans = []
        result = []
        
        def comb(index):
            #you could either pick a value or not pick it
            
            if len(ans) == k:
                result.append(list(ans))
                return
                
                
            if index == n:
                return
            
            comb(index + 1)
            ans.append(array[index])
            comb(index + 1)
            ans.pop()
            
            
        comb(0)
            
                
            
            
        
        return result
        
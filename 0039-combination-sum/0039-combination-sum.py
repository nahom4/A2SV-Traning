class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        #let's preprocess
        new = []
        ans = []
        result = []
        for x in candidates:
            val = target // x
            
            for _ in range(val):
                new.append(x)
                
        def comb(index):
            
            if sum(ans) == target:
               
                result.append(list(ans))
                return
             
            elif sum(ans) > target:
                return 
            
            if index >= len(new):
                return
            ans.append(new[index])
            comb(index + 1)
            
            ans.pop()
            
            while index + 1 < len(new) and new[index] == new[index + 1]:
                index += 1
            comb(index + 1)
        comb(0)
        
        return result
            
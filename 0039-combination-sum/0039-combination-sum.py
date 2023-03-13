class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        ans  = []
                
        def comb(index):
            
            if sum(ans) == target:
               
                result.append(list(ans))
                return
             
            elif sum(ans) > target:
                return 
            
            if index >= len(candidates):
                return
            ans.append(candidates[index])
            comb(index)
            
            ans.pop()
         
            comb(index + 1)
            
        comb(0)
        
        return result
            
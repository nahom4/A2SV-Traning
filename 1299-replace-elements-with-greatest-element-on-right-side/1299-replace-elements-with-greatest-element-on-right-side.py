

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        dic = Counter(sorted(arr,reverse=True))
        
        for i in range(len(arr)):
            
            if dic[arr[i]] <= 1:
                del(dic[arr[i]])
            else:
                dic[arr[i]]-=1
                
            if dic:
                first = next(iter(dic))
                arr[i] = first
            else:
                arr[i] = -1
           
        return arr
        
   
        
        
        
        
        
      
            
        
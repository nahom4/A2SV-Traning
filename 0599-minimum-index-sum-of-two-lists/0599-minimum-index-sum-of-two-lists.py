class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        
        result= []
        sm = len(list1) + len(list2)
        
        
        for i in range(len(list1)):
            for j in range(len(list2)):
                
                if list1[i] == list2[j]:
                    if i+j < sm:
                        if result:
                            result.pop()
                        result.append(list1[i])
                        sm = i+j
                    elif i+j == sm:
                        result.append(list1[i])
                    
        return result
                    
                    
                    
        
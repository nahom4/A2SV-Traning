class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        if (num-3)%3 == 0:
            first  = (num-3)//3
            return [first,first+1,first+2]
            
        else:
            
            return []
            
        
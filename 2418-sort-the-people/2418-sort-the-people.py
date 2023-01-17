class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        dic = {}
        
        for i in range(len(heights)):
            dic[heights[i]] = i
        
        for i in range(len(heights)):
            for j in range(len(heights)-1):
                
                if heights[j] < heights[j+1]:
                    
                    heights[j],heights[j+1] = heights[j+1], heights[j]
                    
        new = []
        
        
        for x in heights:
            new.append(names[dic[x]])
        return new
                    
            
        
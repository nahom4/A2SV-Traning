class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #The longest substing with only two types of fruits
        #dictionary to to keep track of repetion
        dic = defaultdict(int)
        left = 0
        result = 0
        for i in range(len(fruits)):
            
            #add
            dic[fruits[i]] += 1
            
            while left < len(fruits) - 1 and len(dic) > 2:
                dic[fruits[left]] -= 1
                
                if  dic[fruits[left]] == 0:
                  
                    del(dic[fruits[left]])
                left += 1
            
            result = max(result,i - left + 1 )
        
        return result
                    
            
            
            
        
        
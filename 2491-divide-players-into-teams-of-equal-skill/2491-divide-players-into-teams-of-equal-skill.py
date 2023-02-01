class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        i = 0
        j= len(skill)-1
        
        total = []
        product = 0
        
        
        while i < j:
           
            sm = skill[i]+skill[j]
            total.append(sm)
            product += skill[i] * skill[j]
        
            if skill[i]+skill[j] != total[0] :
               
                
                return -1
            i+=1
            j-=1
        return product
        
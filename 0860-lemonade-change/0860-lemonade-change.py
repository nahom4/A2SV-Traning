class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        ten = 0
        twentee = 0
        
        for bill in bills:
            
            if bill == 5:
                five += 1
                
            if bill == 10:
                ten += 1
                five -= 1
                if five < 0:
                    return False
                
            if bill == 20:
                twentee += 1
                
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
                    
                if five < 0:
                    return False
              
                 
        return True
        
        
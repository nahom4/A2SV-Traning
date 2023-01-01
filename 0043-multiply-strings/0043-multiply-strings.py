class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        #to integer
        num3 = 0
        for digit in num1:
            num3 = num3 + 48 - ord(digit)
            num3*= 10
        num3 = num3//10
        num4 = 0
        for digit in num2:
            num4 = num4 + 48 - ord(digit)
            num4*= 10   
        num4//=10
        
        return(str(num3*num4))
            
        
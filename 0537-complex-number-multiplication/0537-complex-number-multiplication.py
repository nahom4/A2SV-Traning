class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        #just use the formula  (ac-cd) + (ad+bc)i where a b c d are the real and the imaginary
        #elements of the two numbers respectively
        
        num1=  num1.split("+")
        num2=  num2.split("+")
        
        a = int(num1[0])
        b = int(num1[1][:-1])
        
        c = int(num2[0])
        d = int(num2[1][:-1])
        
        real = (a*c - b*d)
        imaginary = (a*d + b*c)
        
        return str(real) +"+"+ str(imaginary)+'i'
        
        
        
        
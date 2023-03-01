class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        x_negative = False
        n_negative = False
        
        
        if x < 0:
           
            x_negative = True
            x = -1 * x
        if n < 0:
            n_negative = True
            n = -1 * n
        
        def check_pow(x,n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n > 0:
                if n%5 == 0:
                    n = n//5
                    temp = self.myPow(x,n)
                    return temp*temp*temp*temp*temp
                else:
                    n = n - 1
                    temp = check_pow(x,n)
                    return temp * x
        
        result = check_pow(x,n)
       
     
        if x_negative and n % 2 != 0:
          
            result = -1 * result
        if n_negative:
            result = 1/result
            
        return result
        
        
        
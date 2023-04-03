class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        prime_factor = set()
        
        def calculate(num):
            d = 2
            while d*d <= num:
                
                if num % d == 0:
                    num = num // d
                    prime_factor.add(d)
                else:
                    d += 1
            if num != 1:
                prime_factor.add(num)
        
        for num in nums:
            calculate(num)
           
        return len(prime_factor)
                    
                
                
                
            
            
        
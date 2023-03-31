class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        i = 2
        while i*i  <= n:
            
            #seive
            if is_prime[i]:
                j = i * i
                while j <= n:
                    if j % i == 0:
                        is_prime[j] = False
                        
                    j += i
                        
            if i == 2:
                i += 1
            else:
                i += 2
           
        is_prime[n] = False
            
        return is_prime.count(True)
                
                

            
            
        
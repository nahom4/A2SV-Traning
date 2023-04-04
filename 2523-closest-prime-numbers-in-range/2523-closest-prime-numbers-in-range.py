class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True]*(right + 1)
        primes[0] = primes[1] = False
        prime_factor = []
        
        d = 2
        while d*d <= right:
            
            j = d * d
            if primes[d]:
                while j <= right:

                    if j % d == 0:
                        primes[j] = False

                    j += d
            if d == 2:
                d += 1
            else:
                d += 2

            
        for i in range(left,len(primes)):
            if primes[i]:
                prime_factor.append(i)
        
        diff = float('inf')
        res = [-1,-1]
       
        for i in range(1,len(prime_factor)):
            
            temp_diff = prime_factor[i] - prime_factor[i - 1]
            if temp_diff < diff:
                diff = temp_diff
                res = [prime_factor[i - 1],prime_factor[i]]
            if diff == 2 and prime_factor[i - 1] != 2:
                break
                
        return res
            
                
                
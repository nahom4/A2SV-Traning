class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        prev = "0"
        
        def bit(prev,n,k):
            
            if n == 1:

                return prev[k - 1]
            
          
          
            inverse_s = ''

            for i in prev:

                if i == '0':
                    inverse_s += '1'

                else:
                    inverse_s += '0'

        

            prev = prev + '1' + inverse_s[::-1] 
            return bit(prev,n - 1,k)
        
        return bit(prev,n,k)
            
            
        
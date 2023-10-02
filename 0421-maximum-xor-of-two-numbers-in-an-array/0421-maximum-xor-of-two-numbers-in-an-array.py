
    
class Solution:
    def __init__(self):
        self.pool = {}
        
    def addBit(self,bits):
        pool = self.pool
        N = len(bits)
        for i in range(N):
            if not bits[i] in pool:
                pool[bits[i]] = {}
                
            pool = pool[bits[i]]
         
    def findMaximumXOR(self, nums: List[int]) -> int:
        def calculateBits(num):
            bits = [0] * 32
            for i in range(31,-1,-1): # 0 mask 1
                mask = 1 << i
                bits[i] = 1 if mask & num else 0
            
            return bits[:: -1]
         
        for index,num in enumerate(nums):
            bits = calculateBits(num)
            nums[index] = bits
            self.addBit(bits)
         
        maxValue = float("-inf")
        for bits in nums:
            currValue = 0
            pool = self.pool
            for power,bit in enumerate(bits):
                if bit == 1:
                    if 0 in pool:
                        currValue += 2 ** (31 - power)
                        pool = pool[0]
                    else:
                        pool = pool[1]
                else:
                    if 1 in pool:
                        currValue += 2 ** (31  - power)
                        pool = pool[1]
                        
                    else:
                        pool = pool[0]
                        
            maxValue = max(maxValue,currValue)
        
        return maxValue
                        
            
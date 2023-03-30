class Solution:
    def findComplement(self, num: int) -> int:
        #bit mask of 1 '001'
        start =  1
        temp = num
        while True:
            temp = temp >> 1
            
            num = num ^ start
            start = start * 2
            
            if temp == 0:
                break
                
        return num
            
        
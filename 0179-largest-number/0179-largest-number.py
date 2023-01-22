class Solution:
    def check(self,first,second):
            
            return int(first + second) > int(second+first)
    def largestNumber(self, nums: List[int]) -> str:
        val = []
        #bubble sort
        for x in nums:
            x = str(x)
            
        
        
            val.append(x)
      

       
      
        for i in range(len(val)):
            for j in range(len(val)-1):
                if not self.check(val[j],val[j+1]):

                    val[j], val[j+1] = val[j+1] ,val[j]

        result = ''
        for x in val:
            result+=x

        if result[0] == '0':
            return '0'

           
                
    
        return result
        
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        # i belive i should use a string for this problem
        
        source = '#'.join(source)
        
        result = ""
        target = ""
        
       
        
      
        i = 0
        target_index = 0
        
        while i<len(source)-1:
            
            #lets capture the comments
       
            if not target and source[i] + source[i+1] =='/*':
                target = '/*'
                target_index = i
                
            if not target and source[i] + source[i+1] =='//':
                target = '//'
                
            if not target:
                result+= source[i]
             
            #lets releas the target
            
            if target == '//' and source[i]== "#":
                
                target = ""
                result+='#'
        
                
                
            if target == '/*' and source[i] + source[i+1] == "*/" and i - target_index >1 :
                target = ""
                i+=1
                
            i+=1
            
            
        if not target:
            result += source[-1]
        result =  result.split('#')
        
        new = []
        #lets remove empty strings:
        for x in result:
            if x:
                new.append(x)
                
                
        return new
                
            
            
        
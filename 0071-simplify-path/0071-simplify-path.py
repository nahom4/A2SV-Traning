class Solution:
    def simplifyPath(self, path: str) -> str:
    
    
        
        
        new_path = []
        size = len(path)
       
        
        #remove //
        for i in range(size):
          
            if i < size - 1  and path[i] == '/' and path[i + 1] == '/':
                continue
            
            new_path.append(path[i])
            
        path = ''.join(new_path)
        
        #remove trailing /
        if path[-1] == '/':
            path = path[:-1]
        
       
            
        path = path.split('/')
        
        stack = []
  
        
        for i in range(len(path)):
            #.
            if path[i] == '.':
               
                continue
            if stack and path[i] == '..':
                stack.pop()
                continue
            
            if path[i] != '.' and path[i] != '..':
                    stack.append(path[i])
            
        
        result = '/'.join(stack)
        if result and result[0] == '/':
            return result
        else:
            return '/' + result
      
      
        
        
        
    
        
        
        
        
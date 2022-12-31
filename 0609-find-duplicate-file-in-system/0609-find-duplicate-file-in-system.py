class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        # files are duplicate if they have the same contenent and there content is stored
        #between parenthesis so i should just track and store value in the parenthesis in a
        #dictionary 
        
        directory = defaultdict(list)
        final = []
        
        for direct in paths:
            
            sub = direct.split()
            
            for i in range(1,len(sub)):
                left = sub[i].index("(")
                right = sub[i].index(")")
                
                content = sub[i][left:right+1]
                directory[content].append(sub[0] + "/"+sub[i][:left]) 
      
        for key in directory:
            if len(directory[key]) >=2 :
                final.append(directory[key])
        return final
                
                
                

          
            
      
            
        
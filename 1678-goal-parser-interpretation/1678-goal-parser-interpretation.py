class Solution:
    def interpret(self, command: str) -> str:
        
            word = ""
     
        
            j =0
            while j < len(command):
                if command[j] == "G":
                    word+="G"
                elif command[j] == "(":
                    if command[j+1] == ")":
                        word+= "o"
                        j+=1
                    else:
                        word+="al"
                        j+=3
                        
                j+=1
                
        
            return word                
                    
                
            
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        #let's solve the problem by cases a queen only attacks on the same colum, row or                 #diagonal and if it is not blcoked by othe elements
        
        attack = []
        
        for queen in queens:
            #row attack
            
            if queen[0] == king[0]:
                #now check if any element is blocking the attack
                blocked = False
                for block in queens:
                    if block[0] == queen[0]:
                        if king[1] < block[1]< queen[1]:
                            blocked = True
                            break
                            
                        if queen[1] < block[1]< king[1]:
                            blocked = True
                            break 
                if not blocked:
                    attack.append(queen)
                    
            #column attack
            
            if queen[1] == king[1]:
                #now check if any element is blocking the attack
                blocked = False
                for block in queens:
                    if block[1] == queen[1]:
                        if king[0] < block[0]< queen[0]:
                            blocked = True
                            break
                        if queen[0] < block[0]< king[0]:
                            blocked = True
                            break

                if not blocked:
                    attack.append(queen)
                    
            #diagonal attack
            
            if abs(queen[0]-king[0]) == abs(queen[1]-king[1]):
                
                #four cases to check diagonal blocking
                for block in queens:
                    blocked = False
                    if abs(queen[0]-block[0]) == abs(queen[1]-block[1]):
                        if king[1] < block[1]< queen[1]:
                                if queen[0] < block[0]< king[0]:
                                    blocked = True
                                    break
                                    
                                if king[0] < block[0]< queen[0]:
                                    blocked = True
                                    break
                                    
                        if  queen[1] < block[1]< king[1]:
                            if queen[0] < block[0]< king[0]:
                                    blocked = True
                                    break
                                    
                            if king[0] < block[0]< queen[0]:
                                    blocked = True
                                    break
                if not blocked:
                    attack.append(queen)  
                    
                    
        return attack
                        
                            
                            
                    
                
            
                    
                            
                
        
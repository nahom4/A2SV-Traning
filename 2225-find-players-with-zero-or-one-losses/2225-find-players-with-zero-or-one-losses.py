class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        #let's itirate through mathches and store all players in a set and all loosers
        # in dictionary of losses
        
        players = set()
        loss = dict()
        
        for match in matches:
            players.add(match[0])
            players.add(match[1])
            loss[match[1]] = loss.get(match[1],0) + 1
            
        
        no_loss = []
        one_loss = []
        for player in players:
            if loss.get(player,0) == 0:
                no_loss.append(player)
                
            if loss.get(player,0) == 1:
                one_loss.append(player)
        no_loss.sort()
        one_loss.sort()
                
        return [no_loss,one_loss]
                
            
        
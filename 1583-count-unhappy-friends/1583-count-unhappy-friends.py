class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        #let use dictionaries to make data access easier
        newPref = []
        for i, preference in enumerate(preferences):
            tempDict = dict()
            for i in range(len(preference)):
                tempDict[preference[i]] = i
              
            newPref.append(tempDict)
        
        preferences = newPref
        #let's turn the pair in to some sort of graph
        graph = dict()
        
        for left,right in pairs:
            graph[left] = right
            graph[right] = left
            
        
        count = 0
        for freind in graph: # 0 1
            score = preferences[freind][graph[freind]]
            for key in preferences[freind]:
                if key in graph:
                    pair = graph[key]
                    keyScore = preferences[freind][key]
                    currPref = preferences[key][pair]
                    posPref = preferences[key][freind]
                    
                    if posPref < currPref and keyScore < score:
                        count += 1
                        break
                        
        return count
                    
            
            
        
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        rep = {word : word for word in strs}
        group = {word : {word} for word in strs}
        
        def areSimillar(firstWord,secondWord):
            N = len(firstWord)
            
            diff = 0
            for i in range(N):
                if firstWord[i] != secondWord[i]:
                    diff += 1
              
                if diff > 2:
                    return False
            return diff == 2
                    
        def find(node):
            if rep[node] == node:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(firstWord,secondWord):
            firstWordGroup,secondWordGroup = find(firstWord),find(secondWord)
            
            firstGroup = group[firstWordGroup]
            secondGroup = group[secondWordGroup]
            valid = False
            for word1 in firstGroup:
                for word2 in secondGroup:
                    valid = valid or areSimillar(word1,word2)
                    
            if not valid:
                return
            
            if firstWordGroup == secondWordGroup:
                return
            
            if len(group[firstWordGroup]) < len(group[secondWordGroup]):
                firstWordGroup,secondWordGroup = secondWordGroup,firstWordGroup
                
            rep[secondWordGroup] = firstWordGroup
            group[firstWordGroup].update(group[secondWordGroup])
            
            
        for i in range(len(strs)):
            for j in range(i + 1,len(strs)):
                union(strs[i],strs[j])
            
        groups = set()
        
        for word in strs:
            groups.add(find(word))
            
        return len(groups)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        rep = {letter : letter for letter in s1 + s2}
        rank = {letter : 1 for letter in s1 + s2}
        letters = {letter : {letter} for letter in s1 + s2}
        def find(node):
            if node == rep[node]:
                return node
            
            parent = find(rep[node])
            rep[node] = parent
            
            return parent
        
        def union(first,second):
            firstParent,secondParent = find(first),find(second)
            
            if firstParent == secondParent:
                return 
            
            if rank[firstParent] > rank[secondParent]:
                firstParent,secondParent = secondParent,firstParent
                
            
            rep[secondParent] = firstParent
            rank[firstParent] += rank[secondParent]
            letters[firstParent].update(letters[secondParent])
            
            
        for first,second in zip(s1,s2):
            union(first,second)
            
        ans = []
        for key in letters:
            letters[key] = sorted(list(letters[key]))
            
        for letter in baseStr:
            if not letter in rep:
                ans.append(letter)
                continue
            parent = find(letter)
            ans.append(letters[parent][0])
    
        return "".join(ans)
            
            
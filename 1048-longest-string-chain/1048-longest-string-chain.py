class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        def isPredecessor(A,B):
            
            if not (len(B) == len(A) + 1):
                return False
            
            bumbs = 0
            pointerA = 0
            pointerB = 0
            
            while pointerA < len(A) and pointerB < len(B):
                
                if A[pointerA] != B[pointerB]:
                    bumbs += 1
                    pointerB += 1
                    
                else:
                    pointerA += 1
                    pointerB += 1
                
            if bumbs <= 1:
                return True
            else:
                return False
            
        graph = defaultdict(list)
        N = len(words)
        for i in range(N):
            for j in range(N):
                if isPredecessor(words[i],words[j]):
                    graph[i].append(j)
          
    
        #dfs
        # words = list(map(lambda words : len(word),words))
        cache = {}
        def dfs(node):
            
            if node in cache:
                return cache[node]
            depth = 0
            for child in graph[node]:
                depth = max(dfs(child),depth)
                
            cache[node] = depth + 1
            return cache[node]
        
        finalAns = 1
        for i in range(N):
            finalAns = max(finalAns,dfs(i))
            
        return finalAns
            
                
        
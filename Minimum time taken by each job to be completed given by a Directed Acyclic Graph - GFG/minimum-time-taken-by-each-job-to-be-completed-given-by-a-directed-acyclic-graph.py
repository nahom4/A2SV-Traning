from typing import List
from collections import defaultdict,deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        visited = set()
        queue = deque()
        time = [1] * (n + 1)
        in_degree = [0] * (n + 1)
        
        for u,v in edges:
            graph[u].append(v)
            in_degree[v] += 1
            
        for i in range(1,n + 1):
            if in_degree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            
            for child in graph[node]:
                if child in visited:
                    continue
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    queue.append(child)
                    visited.add(child)
                    time[child] += time[node]
                    
        return time[1 : ]
            
        
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        counter = defaultdict(int)
        
        for edge in edges:
            start,end = edge
            counter[start] += 1
            counter[end] += 1
            
            if counter[start] == len(edges):
                return start
            if counter[end] == len(edges):
                return end
            
            
        
        
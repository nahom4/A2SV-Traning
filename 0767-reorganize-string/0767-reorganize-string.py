class Solution:
    def reorganizeString(self, s: str) -> str:

        countdict = Counter(s)
        heap = []
        
        for key in countdict:
            count = countdict[key]
            heapq.heappush(heap,(-count,key))
            
          
        answer = []
        while heap:
            
            count,currChar = heapq.heappop(heap)
            
            if answer and answer[-1] == currChar:
                if not heap:
                    return ""
                nextCount,nextChar = heapq.heappop(heap)
                heapq.heappush(heap,(count,currChar))
                count,currChar = nextCount,nextChar
                
            count += 1
            if count != 0:
                heapq.heappush(heap,(count,currChar))
           
            answer.append(currChar)
            
        return "".join(answer)
                
                
            
            
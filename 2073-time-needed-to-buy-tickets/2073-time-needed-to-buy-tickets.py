class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        result = 0
        n = len(tickets)
        for i in range(n):
            #for value that come before index k
            if i <= k:
                if tickets[i] > tickets[k]:
                    result += tickets[k]
                else:
                    result += tickets[i]
            else:
                if tickets[i] >  tickets[k] - 1:
                    result += tickets[k] - 1
                else:
                    result += tickets[i]
                
            #for values that come after index k
        return result
           
                
      
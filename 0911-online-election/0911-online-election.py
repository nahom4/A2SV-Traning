
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        self.persons = persons
        self.times  = times
        self.new = []
        
        #we should do some pre processing
        for i in range(len(self.persons)):
            count = Counter(self.persons[:i + 1])
            count_values = list(count.values())
            mx_value = max(count_values)
            target = set()
            for key in count:
                if count[key] == mx_value:
                    target.add(key)

            for j in range(i ,-1,-1):
                if self.persons[j] in target:
                    self.new.append(persons[j])
                    break

     

    def q(self, t: int) -> int:
        
        #I have to find the index where this time should fit in to
        low = -1
        high = len(self.times)
        
        while high > low + 1:
            md = low + (high - low) // 2
            if self.times[md] <= t:
                low = md
            else:
                high = md
                
      
        return self.new[low]
            
                
        
            
    
     
      
      
            
            
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
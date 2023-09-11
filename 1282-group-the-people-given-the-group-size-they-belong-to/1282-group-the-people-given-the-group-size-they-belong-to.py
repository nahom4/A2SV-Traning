class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        #let's optimize using a dictionary
        cache = defaultdict(list)
        ans = []
        for index,size in enumerate(groupSizes):
            if cache[size]:
                if len(cache[size]) < size:
                    cache[size].append(index)
                    
                else:
                    ans.append(cache[size])
                    cache[size] = [index]
            else:
                cache[size] = [index]
                
                
        for key in cache:
            if cache[key]:
                ans.append(cache[key])
                     
        return ans
                
                
        
        
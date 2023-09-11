class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        #let's use double for loop
        ans = [[-1]]
        for index,size in enumerate(groupSizes):
            found = False
            for group in ans:
                if group[0] == size and len(group) - 1 < size:
                    found = True
                    group.append(index)
                    break
            if not found:
                newGroup = [size,index]
                ans.append(newGroup)
                
        newAns = []
                
        for group in ans:
            if group[0] != -1:
                newAns.append(group[1 : ])
            
            
        return newAns
                
        
        
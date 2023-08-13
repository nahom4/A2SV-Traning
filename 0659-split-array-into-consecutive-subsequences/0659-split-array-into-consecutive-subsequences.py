class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        heapq.heapify(nums)
        listOfSubSequences = []
        
        while nums:
            currNum = heapq.heappop(nums)
            index = len(listOfSubSequences) - 1
            
            while index >= 0:
                if listOfSubSequences[index][-1] == currNum - 1:
                    break
                index -= 1
                    
            if index == -1:
                listOfSubSequences.append([currNum])
            else:
                listOfSubSequences[index].append(currNum)
                
                
        for subSequence in listOfSubSequences:
            if len(subSequence) < 3:
                return False
            
        return True
        
        
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        greater = []
        equal = []
        
        for x in nums:
            if x == pivot:
                equal.append(x)
            if x> pivot:
                greater.append(x)
            if x< pivot:
                less.append(x)
                
        return less+equal + greater
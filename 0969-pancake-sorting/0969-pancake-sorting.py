class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        l = len(arr)
        res = []
        for x in range(len(arr)):
            mx = max(arr[:l-x])
            f = arr[:l-x].index(mx)+1
            arr[:f] = reversed(arr[:f])
            res.append(f)
            arr[:l-x] = reversed(arr[:l-x])
            res.append(l-x)

        return res
            

        
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        ans = []
        for value in candies:
            if value + extraCandies >= maxCandy:
                ans.append(True) 
            else:
                ans.append(False)
                
        return ans
        
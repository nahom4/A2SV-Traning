class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        runningSum = 0
        maxHeight = float("-inf")
        for diff in gain:
            runningSum += diff
            maxHeight = max(maxHeight,runningSum)
        
        return maxHeight if maxHeight > 0 else 0
        
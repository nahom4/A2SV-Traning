class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year = [0] * 101
        lowerBound = 1950
        for start,end in logs:
            year[start - lowerBound] += 1
            year[end - lowerBound] -= 1

        for i in range(1,101):
            year[i] += year[i - 1]

        mx = max(year)
        return year.index(mx) + lowerBound
            
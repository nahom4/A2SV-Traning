class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        
        max_value = float('-inf')
        cache = defaultdict(int)
        for i in range(len(values) - 1,-1,-1):
            max_value = max(max_value, values[i] + cache[i + 1] - 1)
            cache[i] = max(values[i],cache[i + 1] - 1)
            
        return max_value
            
            
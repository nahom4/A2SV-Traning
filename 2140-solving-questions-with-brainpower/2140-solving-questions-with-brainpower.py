class Solution(object):
    def mostPoints(self, questions):
        """
        :type questions: List[List[int]]
        :rtype: int
        """
        cache = defaultdict(int)
        for i in range(len(questions) - 1,-1,-1):
            point,bp = questions[i]
            cache[i] = max(point + cache[i + bp + 1],cache[i + 1])
            
        return max(cache.values())
            
        
class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        cache = defaultdict(int)
        
        for i in range(len(arr) - 1,-1,-1):
            cache[arr[i]] = 1 + cache[arr[i] + difference]
            
        return max(list(cache.values()))
        

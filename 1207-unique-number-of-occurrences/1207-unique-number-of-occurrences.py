class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        ct = Counter(arr)
        st = set()
        for key in ct:
            if not ct[key] in st:
                st.add(ct[key]) 
            else:
                return False
            
        return True
        
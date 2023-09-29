class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        ct1,ct2 = Counter(word1),Counter(word2)
        if set(word1) != set(word2):
            return False
        ctA,ctB = Counter(list(ct1.values())),Counter(list(ct2.values()))
        for key in ctA:
            if ctA[key] != ctB[key]:
                return False
        return True
        
            
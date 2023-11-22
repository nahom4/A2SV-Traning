class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        #if the two letters identical they could be center peice
        ct = Counter()
        maxCenter = 0
        ans = 0
        for val in words:
            reverse = val[:: -1]
            if ct[reverse] > 0:
                ans += 4
                ct[reverse] -= 1
            else:
                ct[val] += 1
    
        for val in ct:
            if val[0] == val[1] and ct[val] > 0:
                ans += 2
                break

        return ans



        
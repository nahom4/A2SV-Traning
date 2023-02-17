class Solution:
    def compress(self, chars: List[str]) -> int:
        # two pointers i and j
        i = 0
        j = 1
        count = 1
        s = ''
        for x in range(len(chars)-1):
            if chars[i] == chars[j]:
                j+=1
                count +=1
            else:
                if count != 1:
                    s = s+chars[i]+str(count)
                else:
                    s = s+chars[i]
                count = 1
                i = j
                j+=1
        if count!=1:
            s =  s+chars[i] + str(count) 
        else:
            s = s + chars[i]
        chars.clear()
        for x in s:
            chars.append(x)

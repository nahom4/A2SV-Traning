class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int "11106"
        """
        cache = defaultdict(int)
        def helper(i):
            
            if int(s[i]) == 0:
                return 0
            
            if i + 1 < len(s):
                if int(s[i : i + 2]) <= 26:
                    first = cache[i + 1]
                    second = 1
                    if i + 2 in cache:
                        second = cache[i + 2]
                    
                        
                    return  first + second
                else:
                    return cache[i + 1]
                
            else:
                return 1
                
                
            
        for i in range(len(s) -1,-1,-1):
            cache[i] = helper(i)
            
        return cache[0]
            
            

       
            
        
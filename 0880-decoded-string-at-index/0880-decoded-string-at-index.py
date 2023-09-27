class Solution(object):
    def decodeAtIndex(self, s, k):
        """
            :type s: str
            :type k: int
            :rtype: str 
                    #if I didn't get the answer it means I am in a copy 
        #so I need to go back I know the last position before the copy last so
        
        #when I go back how do I know if i am in an original index or a copy
        #original index's are not more than a hundred so we could use a set
        #store them there so if an index is not in the set it means it is a copy
        # which means I need to translate to an original index using the translation right in front of it which I can use a stack to access
        
        """
    
        #I need to know the end position so that I go to the 
        #front
        N = len(s)
        l = 0
        last = None
        real = dict()
        stack = []
        mp = dict()
        for i in range(N):#leetleetcode
            if s[i].isalpha():
                l += 1 
                real[l] = s[i]
      
            else:
                stack.append((int(s[i]) - 1,l))
                newLocation =  l * (int(s[i]) -1) + l
                mp[l] = newLocation
                l = newLocation
            if l > k:
                break   
     
        def recursion(k): #haha|haha
     
            if k in real:
                return real[k]
            
            for key in mp:
                if key <= k and k <= mp[key]: #this means k is in this range 
                    break
            diff = k - key
            if diff < key:
                nxtIndex = k - key
            else:
                div = diff // key 
                nxtIndex = k - (key) * div
   
            return recursion(nxtIndex)
        
        return recursion(k)
            
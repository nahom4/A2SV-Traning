from collections import OrderedDict
import copy
class Solution:
    def partitionLabels(self, s):
        #let's prepare a dictionary
        dic = OrderedDict()
        arr = []
        for x in s:
            dic[x] = dic.get(x,0) + 1
        j = 0 
        temp = copy.deepcopy(dic) 
        st = set() 
        for y in s:
            
            dic[y] = dic[y]-1
            temp[y]-=1
            st.add(y)
            print(st)
            count = 0
            j+=1
            for x in st:
                if dic[x] == 0:
                    count +=1

            if count == len(st):
                for x in st:
                    del(dic[x])
                arr.append(j)
                st.clear()
                j=0
            
        
        return arr 
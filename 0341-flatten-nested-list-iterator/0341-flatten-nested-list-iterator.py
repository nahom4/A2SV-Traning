# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

#flatten the whole list and store it in another list and whenever asked for next #return from that list let's use recursion
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.flattnedList = []
        self.pointer = 0
        self.flatten(nestedList)
        self.limit = len(self.flattnedList)
   
    def flatten(self,nestedList):
        def recursive(nestedList):
            
            if isinstance(nestedList, list):
                for obj in nestedList:
                        recursive(obj)
                 
                return
            val = nestedList.getInteger()
            if val != None:
                self.flattnedList.append(val)
                
            ls = nestedList.getList()
            if ls:
                recursive(ls)
                
        recursive(nestedList)
        
        print(self.flattnedList)
        # print(nestedList)
        
    
    def next(self) -> int:
        val = self.flattnedList[self.pointer]
        self.pointer += 1
        return val
    
    def hasNext(self) -> bool:
        if self.pointer < self.limit:
            return True
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
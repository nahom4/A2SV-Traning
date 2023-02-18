class Node:
    def __init__(self,value,next_node):
        
        self.value = value
        self.next = next_node


class MyLinkedList:

    def __init__(self):
        
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp.value
        

    def addAtHead(self, val: int) -> None:
        
        self.head = Node(val,self.head)
        self.size +=1
        

    def addAtTail(self, val: int) -> None:
        
        if self.size == 0:
            self.head = Node(val,None)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(val,None)
        self.size+=1
            
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            if index == 0:
                self.head = Node(val,self.head)
            else:
                temp = self.head
                prev= self.head

                for _ in range(index):
                    prev = temp
                    temp = temp.next
                prev.next= Node(val,temp)
            self.size +=1
        

    def deleteAtIndex(self, index: int) -> None:
         if index<self.size:
            if index==0:
                self.head = self.head.next
            else:
                temp = self.head
                prev= self.head

                for _ in range(index):
                    prev = temp
                    temp = temp.next
                prev.next= temp.next
            self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
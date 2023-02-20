# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        size = 0
      
        dummy = ListNode(0)
        dummy.next = head
        temp1 = dummy
        
        while temp:
            size += 1
            temp = temp.next
            
      
        count = 0
        diff = size-n
      
        while temp1 and  count < diff  :
            temp1 = temp1.next
            count += 1
        temp1.next = temp1.next.next
        
        return dummy.next
        
      
            
        
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            
        dummyNode = ListNode()
        dummyNode.next = head
        fast = slow = dummyNode
        prev = None
        while fast and fast.next:# dummy -> head 
            fast = fast.next.next
            prev = slow
            slow = slow.next
           
        nxtVal = None
        if slow and slow.next:
            nxtVal = slow.next.next
            
        if count % 2 != 0:
            prev.next = slow.next 
        else:
            slow.next  = nxtVal
        return dummyNode.next
    
    
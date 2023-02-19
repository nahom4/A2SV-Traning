# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode(0)
        curr = new_head
        first = list1
        second = list2
        
        while first != None and second != None:
            
            
            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next
            curr = curr.next
        if first:
            curr.next = first
        if second:
            curr.next = second
                
            
        return new_head.next    
          
                
            
           
                  
                
            
                
                
        
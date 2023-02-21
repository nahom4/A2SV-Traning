# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        #first let's find their sizes
        
#         temp = l1
#         size = 0
#         while temp:
#             size +=1
#             temp = temp.next
            
           
#         temp = l2
#         size1 = 0
#         while temp:
#             size1 +=1
#             temp = temp.next
#         if size < size1:
            
#             while size < size1:
#                 l1 = ListNode(0,l1)
#                 size+=1
#         elif size1 == size:
#             pass
             
#         else:
#              while size1 < size:
#                 l2 = ListNode(0,l2)
#                 size1+=1
        carry = 0
        dummy = ListNode(0)
        temp = dummy
        temp2 = l1
        temp3 = l2
        
        while temp2 and temp3:
            sm = temp2.val + temp3.val + carry
            if sm > 9:
                carry = 1
                sm = sm - 10
            else:
                carry = 0
            temp.next = ListNode(sm) 
            temp = temp.next
            temp2 = temp2.next
            temp3 = temp3.next
            
        while temp2:
            
            sm = temp2.val  + carry
            if sm > 9:
                carry = 1
                sm = sm - 10
            else:
                carry = 0
            temp.next = ListNode(sm) 
            temp = temp.next
            temp2 = temp2.next
        while temp3:
            sm = temp3.val  + carry
            if sm > 9:
                carry = 1
                sm = sm - 10
            else:
                carry = 0
            temp.next = ListNode(sm) 
            temp = temp.next
            temp3 = temp3.next
            
        if carry == 1:
            temp.next = ListNode(1) 
            
            
        return dummy.next
            
            
            
            
            
            
            
        
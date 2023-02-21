# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd = True
        temp = head
        odd_pointer = head
        even_pointer = None
        while temp:
            
            if odd and temp == head:
                odd_pointer = head
                temp = temp.next
                odd = False
            elif odd:
                
                rest = temp.next
                middle = odd_pointer.next
                odd_pointer.next= temp
                temp.next = middle
                even_pointer.next = rest
                odd_pointer = odd_pointer.next
                odd = False
                temp = rest
            else:
                odd = True
                even_pointer = temp
                temp = temp.next
            
                
          
        return head
                
        
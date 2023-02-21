# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        #find the middl element
        fast = head
        slow = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            

       
        #Now let's reverse the list starting from the middle element
        temp = slow 
        
        
        
        
        prev = None
        while temp:
            rest = temp.next
            curr = temp
            curr.next = prev
            prev = curr
            middle_head = curr
           
          
            temp = rest
        
        first = head
        second = middle_head
        mx_sum  = -math.inf
        
        while first and second:
            
            mx_sum = max(mx_sum,first.val + second.val)
            first = first.next
            second = second.next
            
    
         
        
      
        
        return mx_sum
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        temp = head
        
        #check size
        
        while temp:
            temp = temp.next
            size += 1
        if size == 0:
            return None
        k = k%size
        if not head:
            return head
        
        for _ in range(k):
            
            temp = head
            value= head.val
            while temp:
                temp_value = temp.val
                temp.val = value
                value = temp_value
                temp = temp.next
                
            head.val = value
        return head
                
            
            
        
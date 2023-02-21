# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp = head
        visited = set()
        while temp and temp.next:
            
            visited.add(temp.val)
            if  temp.next.val in visited:
              
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
                
        
            
            
        
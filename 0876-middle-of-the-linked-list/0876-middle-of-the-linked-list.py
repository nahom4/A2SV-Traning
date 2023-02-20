# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        fast_node = head
        slow_node = head
        while fast_node and fast_node.next:
            
            fast_node = fast_node.next.next
            slow_node = slow_node.next
        return slow_node
        
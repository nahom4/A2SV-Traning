# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #let's build it recursevely
        dummy_node = ListNode(0)
        temp1 = list1
        temp2 = list2
        def build(start,first,second):
            
            if first is None:
                if second:
                    start.next = second
                    
                return start
            if second is None:
                if first:
                    start.next = first
                return start
            
            if first.val < second.val:
                start.next = first
                first = first.next
                start = start.next
                build(start,first,second)
            else:
                start.next = second
                second = second.next
                start = start.next
                build(start,first,second)
                
        build(dummy_node,temp1,temp2)
        return dummy_node.next

                
            
            
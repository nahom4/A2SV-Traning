# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        stack = []
        current = head
        count = 0
        size = 0
        
        while current:
            current = current.next
            size += 1
          
        result = [0] * size
        current = head
        while current:
            while stack and stack[-1][0] < current.val:
                val = stack.pop()
                result[val[1]] = current.val 
            
            stack.append([current.val,count])
            current = current.next
            count += 1
        return result
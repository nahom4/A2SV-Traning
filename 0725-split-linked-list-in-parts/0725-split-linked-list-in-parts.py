# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        #count
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
             
        remainder = count %  k
        size = count // k
        
        #segment
        ans = []
        curr = head
        
        def calculateSize():
            nonlocal remainder
            segmentSize = size
            if remainder > 0:
                segmentSize += 1
                remainder -= 1
            
            return segmentSize
        
        segmentSize = calculateSize()
        segmentHead = curr
        while curr:
            segmentSize -= 1
            nxtNode = curr.next
            
            if segmentSize <= 0:
                ans.append(segmentHead)
                curr.next = None
                segmentHead = nxtNode
                segmentSize = calculateSize()
             
            curr = nxtNode
        while len(ans) < k:
            ans.append(None)
            
        return ans
                
            
            
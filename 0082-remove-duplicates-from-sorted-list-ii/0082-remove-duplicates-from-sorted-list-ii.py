# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        visited = set()
        duplicate =  set()
        while temp and temp.next:
            
            visited.add(temp.val)
            if  temp.next.val in visited:
                duplicate.add(temp.next.val)
              
                temp.next = temp.next.next
            else:
                temp = temp.next
                
                
        temp = head
       
      
        while temp and temp.next:
          
            
              if temp == head and temp.val in duplicate:
               
                    head = temp.next
                    temp = temp.next
            
              elif  temp.next.val in duplicate:
                
                    
                    temp.next = temp.next.next
                    
               
              else:
                     temp = temp.next
        if head and head.val in duplicate:
            return None
            
             
        return head
        
        
        
        
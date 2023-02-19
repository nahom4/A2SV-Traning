# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
      
        temp = head
        less = None
        greater = None
        while temp != None:
            
            if temp.val < x and not less:
                less = ListNode(temp.val,None)
            elif temp.val < x and less:
                
                temp1= less
                while temp1.next != None:
                    temp1= temp1.next
                   
              
                temp1.next = ListNode(temp.val,None)
            elif temp.val >= x and not greater:
                 greater = ListNode(temp.val,None)
            elif temp.val >= x and  greater:
                temp2 = greater
                while temp2.next != None:
                    temp2= temp2.next
                temp2.next = ListNode(temp.val,None)
            temp = temp.next
                
        temp3 = less
        while temp3 and temp3.next != None:
            temp3 = temp3.next
            
        if temp3:
            
            temp3.next = greater
        if not less:
            return greater
        return less
    
                
                
            
            
            
            
            
          
          
                

                
        
          
                
           
         
          
    
           
            
            
            
                
           
        
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #first let's reverse the linked list
        
        prev = None
     
        temp = head
        
       
     
        while temp:
            
            new_node= ListNode(temp.val,None)
            new_node.next = prev
            prev = new_node
            temp = temp.next
                
        temp1= head
        temp2 = new_node
        
        while temp1 and temp2:
            
            if temp1.val != temp2.val:
              
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True
        
        
        
        
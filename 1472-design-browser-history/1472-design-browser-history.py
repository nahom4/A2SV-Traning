class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        

class BrowserHistory:

    def __init__(self, homepage: str):
        
        self.homepage = ListNode(homepage) 
        self.current = self.homepage
        
        

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url)
        self.current = self.current.next
        
        

    def back(self, steps: int) -> str:
        
        fast = self.homepage
        slow = self.homepage
        
        while  fast != self.current:
            if steps >0:
                steps-=1
            else:
                slow =  slow.next
            fast = fast.next
        self.current = slow
        return slow.val

        

    def forward(self, steps: int) -> str:
        
        temp = self.current
        while temp.next and steps > 0:
            temp = temp.next
            steps -= 1
        self.current = temp
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
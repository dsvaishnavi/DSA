class Node:
    def __init__(self,val=0,next=None):
        self.val=self
        self.next=next
        
    def Duplicate(head):
        current = head
        
        while current:
            runner=current
        while runner:
            if runner.val.next == current.val:
                runner=runner.next.next
            else:
                runner=runner.next
        current=current.next
        print(head)
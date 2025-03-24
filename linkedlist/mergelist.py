

class Listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def Traverse(head):
        temp=head
        while temp:
            print(temp.val ,end="-->")
            temp=temp.next
        print("None")
        
head=Listnode(10)
head.next=Listnode(1)
head.next.next=Listnode(2)
Traverse(head)
        

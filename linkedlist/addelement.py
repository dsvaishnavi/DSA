# def insert_at_head(head, val):
#     new_node = ListNode(val)
#     new_node.next = head  # New node points to old head
#     return new_node  # New node becomes the head



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
        
        
def insert_at_head(head, val):
    new_node = Listnode(val)
    new_node.next = head  # New node points to old head
    return new_node  # New node becomes the head
        
head=Listnode(10)
head.next=Listnode(1)
head.next.next=Listnode(2)
head.next.next.next=Listnode(3)
Traverse(head)
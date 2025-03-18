class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

#assign value
    
node1=Node(10)
node2=Node(10)
node3=Node(20)

#link it

node1.next=node2
node2.next=node3

current=node1
while current:
    check=current.next
    while check:
        check.val==current.val
        print("duplicate")



def PrintList(head):
    current=head
    while current:
        print(current.val,end="-->")
        current=current.next
    print("end")
    if head == current:
        head=current.next
PrintList(node1)


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def rev(self):
        prev=None
        curr=self.head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
        
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="-->")
            temp=temp.next
        print("none")
l1=Linkedlist()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.rev()
l1.display()

class Node:
    def __init__(self, val=0, next=None):
        self.val = val  
        self.next = next  
# Assign values
node1 = Node(10)
node2 = Node(10)
node3 = Node(20)

# Link nodes
node1.next = node2
node2.next = node3

# Function to remove duplicates from sorted linked list
def Duplicate(head):
    if not head:
        return None
    curr = head
    while curr and curr.next:
        if curr.next.val == curr.val:
            curr.next = curr.next.next  # ✅ Skip duplicate node
        else:
            curr = curr.next  # ✅ Move to next node if no duplicate
    return head

# Function to print linked list
def PrintList(head):
    current = head
    while current:
        print(current.val, end=" --> ")
        current = current.next
    print("end")

# Remove duplicates before printing
node1 = Duplicate(node1)  
PrintList(node1)

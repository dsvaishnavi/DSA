class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create linked list nodes
node1 = Node(10)
node2 = Node(10)
node3 = Node(20)
node4 = Node(30)
node5 = Node(20)

# Link nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1

while current:
    runner = current  # A second pointer to check future nodes
    while runner.next:  # Traverse remaining nodes
        if runner.next.val == current.val:  # If duplicate is found
            runner.next = runner.next.next  # Remove the duplicate node
        else:
            runner = runner.next  # Move to next node
    current = current.next  # Move main pointer forward

# Print the linked list without duplicates
current = node1
while current:
    print(current.val, end=" --> ")
    current = current.next
print("None")

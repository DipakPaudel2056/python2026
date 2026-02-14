# so we know what is linked list 
# singly linked list means the linked list with nodes having a pointer pointing towards next node
# last item in the linked list points to null

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

currentNode = node1
while currentNode:
    print(currentNode.data, end="->")
    currentNode = currentNode.next
print("null")
# this is also a simple linked list,
# instead of one pointer, it's node has two pointer pointing towards prev and next
# last node in this ll have prev pointer but not next pointer, 
# first node  has next pointer but not prev pointer

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

currentNode = node1
while currentNode:
    print(currentNode.data,end="->")
    currentNode = currentNode.next
print("Null")   
  
currentNode = node3
while currentNode:
    print(currentNode.data,end = "->")
    currentNode = currentNode.prev 
print("Null")   
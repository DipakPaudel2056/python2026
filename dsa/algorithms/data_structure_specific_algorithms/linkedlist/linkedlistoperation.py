class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node7 = Node(7)

node1.next = node2
node2.next = node3
node3.next = node4

def traverseLinkedList(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="->")
        currentNode = currentNode.next
    print("null")

def findMin(head):
    minvalue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minvalue:
            minvalue = currentNode.data
        currentNode = currentNode.next
    return minvalue

def findMax(head):
    maxValue = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data > maxValue:
            maxValue = currentNode.data
        currentNode = currentNode.next
    return maxValue

def deleteNode(head,nodetodelete):
    if head == nodetodelete:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode != nodetodelete:
        currentNode = currentNode.next
    if currentNode.next is None:
        return head
    currentNode.next = currentNode.next.next
    
    return head
        
def insertNode(head,nodetoInsert,position):
    if position == 1:
        nodetoInsert.next = head
        return nodetoInsert
    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next
    nodetoInsert.next = currentNode.next
    currentNode.next = nodetoInsert
    return head
    

print(findMin(node1))
print(findMax(node1))
insertNode(node1,node7,2)
traverseLinkedList(node1)
    

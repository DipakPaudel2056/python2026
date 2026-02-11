# tree is the data structure which is not linear like linked list
# in linked list there is only one next element, but in tree the nodes can have multiple nodes and it is heirarchical
# there are different types of tree, among them binary search tree is the most popular one
# let's see how they are implemented

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
root  = TreeNode("R")
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodec = TreeNode('c')
noded = TreeNode('d')
nodeE = TreeNode('e')
nodef = TreeNode('f')

root.left = nodeA
root.right = nodeB

nodeA.left = nodec
nodeA.right = noded

nodeB.left = nodeE
nodeB.right = nodef

def print_tree(node, prefix="", is_left=False):
    """Recursively prints the tree structure to the console."""
    if node is None:
        return

    # Print the right child first (to get top-down appearance when rotated)
    print_tree(node.right, prefix + ("|   " if is_left else "    "), False)

    # Print the current node
    print(prefix + ("|-- " if is_left else "\\-- ") + str(node.data))

    # Print the left child
    print_tree(node.left, prefix + ("|   " if is_left else "    "), True)


# here we have created a binary tree, let's traverse in this tree
# Breadth first search()
# when the nodes on the same level are visited before going to the next level in the tree. Tree is explored in more sideways direction
# solution using queue
def levelOrder(root):
    if root is None:
        return []
    q= []
    res = []
    
    q.append(root)
    curr_level = 0
    
    while q:
        len_q = len(q)
        res.append([])
        for _ in range(len_q):
            node = q.pop(0)
            res[curr_level].append(node.data)
            if  node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        curr_level += 1
    return res
print (levelOrder(root=root),"-->using queue")

#solution using recursion
def levelorderrec(root,level,res):
    if root is None:
        return
    if len(res) <= level:
        res.append([])
    res[level].append(root.data)
    levelorderrec(root.left,level+1,res)
    levelorderrec(root.right,level+1,res)

def recursion_level_order(root):
    res = []
    levelorderrec(root,0,res)
    return res

print(recursion_level_order(root=root),"-->using recursion")

# Depth first search()
# when the traversal moves down the tree all the way to the leaf nodes, exploring the tree branch by branch in downwards direction.

# solution using inorder traversal
dfsroot = TreeNode(1)
dfsroot.left = TreeNode(2)
dfsroot.right = TreeNode(3)
dfsroot.left.left = TreeNode(4)
dfsroot.left.right = TreeNode(5)
dfsroot.right.right = TreeNode(6)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data),
        inorder_traversal(root.right)
        
print(inorder_traversal(dfsroot),"===>inorder traversal")

# preorder traversal
# 1. visit the root
# 2. Traverse the left subtree 
# 3. Traverse the right subtree


# postorder traversal
# 1. traverse the left subtree
# 2. traverse the right subtree
# 3. visit the root
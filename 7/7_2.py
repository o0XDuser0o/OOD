class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data,root):
        if root == None:
            root = Node(data)
        elif data < root.data:
            root.left = self.insert(data,root.left)
        else:
            root.right = self.insert(data,root.right)
        return root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def treelevel(self,node,level = -1):
        if node == None:
            return level
        level += 1
        right = self.treelevel(node.right,level)
        left = self.treelevel(node.left,level)
        if right > left:
            return right
        elif right < left:
            return left
        return right

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.root = T.insert(i,T.root)
#T.printTree(T.root)
print("Height of this tree is :",T.treelevel(T.root))
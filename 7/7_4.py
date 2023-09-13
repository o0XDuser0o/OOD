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

    def insert(self,data):
        self.root = self._insert(data,self.root)

    def _insert(self,data,root):
        if root == None:
            root = Node(data)
        elif data < root.data:
            root.left = self._insert(data,root.left)
        else:
            root.right = self._insert(data,root.right)
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
    
    def deleteNode(self,data):
        self.root,c = self._deleteNode(self.root,data)
        return c

    def _deleteNode(self,root,data):
        checker = False
        if root == None:
            return root,False
        if data > root.data:
            root.right,checker = self._deleteNode(root.right,data)
        elif data < root.data:
            root.left,checker = self._deleteNode(root.left,data)
        else:
            checker = True
            if root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
            else:
                n = root.right
                while n.left != None:
                    n = n.left
                root.data = n.data
                root.right,checker = self._deleteNode(root.right,n.data)
        return root,checker

t = BST()
for act in input("Enter Input : ").split(","):
    if act[:1] == "i":
        print("insert",act[2:])
        t.insert(int(act[2:]))
        t.printTree(t.root)
    elif act[:1] == "d":
        print("delete",act[2:])
        c = t.deleteNode(int(act[2:]))
        if not c:
            print("Error! Not Found DATA")
        t.printTree(t.root)
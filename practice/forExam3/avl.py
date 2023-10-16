class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None    
        self.right = None
    
    def __str__(self) -> str:
        return str(self.data)

class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)
    
    def _insert(self,root : Node,data):
        if root == None:
            return Node(data)
        if root.data < data:
            root.right = self._insert(root.right,data)
        else:
            root.left = self._insert(root.left,data)
        root = self.rebalance(root)
        return root
    
    def printTree(self):
        self._printTree(self.root)
    
    def _printTree(self,root:Node,level = 0):
        if root != None:
            self._printTree(root.right,level+1)
            print("    "*level,root)
            self._printTree(root.left,level+1)
    
    def deleteNode(self,data):
        self.root = self._deleteNode(self.root,data)

    def _deleteNode(self,root:Node,data):
        if root == None:
            return None
        if root.data < data:
            root.right = self._deleteNode(root.right,data)
        elif root.data > data:
            root.left = self._deleteNode(root.left,data)
        else:
            if root.right == None:
                root = root.left
            elif root.left == None:
                root = root.right
            else:
                n = root.right
                while n.left != None:
                    n = n.left
                root.data = n.data
                root.right = self._deleteNode(root.right,n.data)
            root = self.rebalance(root)
        return root
    
    def getHeight(self,root:Node,level = 0):
        if root == None:
            return level
        level += 1
        right = self.getHeight(root.right,level)
        left = self.getHeight(root.left,level)
        if right > left:
            return right
        else:
            return left
        
    def balance(self,root:Node):
        if root == None or (root.right == None and root.left == None):
            return 0
        elif root.right == None:
            return self.getHeight(root.left)
        elif root.left == None:
            return self.getHeight(root.right)*-1
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotate(self,root):
        x = root
        y = root.right
        x.right = y.left
        y.left = x
        return y

    def rightRotate(self,root:Node):
        x = root
        y = root.left
        x.left = y.right
        y.right = x
        return y
    
    def rebalance(self,root:Node):
        bal = self.balance(root)
        if bal > 1:
            if self.balance(root.left) <= -1:
                root.left = self.leftRotate(root.left)
            root = self.rightRotate(root)
        elif bal < -1:
            if self.balance(root.right) >= 1:
                root.right = self.rightRotate(root.right)
            root = self.leftRotate(root)
        return root
        
        



    
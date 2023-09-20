def nameValue(val):
    return sum([ord(c) for c in val ])

class TreeNode(object):
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class AVL_Tree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self, root:TreeNode, data):
        if root == None:
            root = TreeNode(data)
        elif nameValue(data) < nameValue(root.data):
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        root  = self.getBalance(root)
        return root

    def delete(self, data):
        self.root = self._delete(self.root,data)

    def _delete(self,root:TreeNode,data):
        if root == None:
            return root
        elif nameValue(data) < nameValue(root.data):
            root.left = self._delete(root.left,data)
        elif nameValue(data) > nameValue(root.data):
            root.right = self._delete(root.right,data)
        else:
            if root.left == None:
                root = root.right
            elif root.right == None:
                root = root.left
            else:
                n = root.right
                while n.left != None:
                    n = n.left
                root.data = n.data
                root.right = self._delete(root.right,n.data)
        root  = self.getBalance(root)
        return root

    def leftRotate(self, z:TreeNode):
        r = z.right
        z.right = r.left
        r.left = z
        return r

    def rightRotate(self, z:TreeNode):
        l = z.left
        z.left = l.right
        l.right = z
        return l

    def getHeight(self, root:TreeNode,level = 0):
        if root == None:
            return level
        level += 1
        right = self.getHeight(root.right,level)
        left = self.getHeight(root.left,level)
        if right > left:
            return right
        elif right < left:
            return left
        return right

    def getBalance(self, root:TreeNode):
        bal = self.balanceLevel(root)
        if bal > 1:
            if self.balanceLevel(root.left) == -1:
                root.left = self.leftRotate(root.left)
            root = self.rightRotate(root)
        if bal < -1:
            if self.balanceLevel(root.right) == 1:
                root.right = self.rightRotate(root.right)
            root = self.leftRotate(root)
        return root
    
    def balanceLevel(self,root:TreeNode):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 0
        elif root.left == None:
            return -1*self.getHeight(root.right)
        elif root.right == None:
            return self.getHeight(root.left)
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printTree(self):
        self._printTree(self.root)

    def _printTree(self, root:TreeNode, level=0):
        if root != None:
            print("    "*level + str(root) + " (" + str(nameValue(root.data)) + ")")
            if root.left == None or root.right == None:
                if root.left == None and root.right != None:
                    print("    "*(level+1)+"*")
                    self._printTree(root.right,level+1)
                elif root.left != None and root.right == None:
                    self._printTree(root.left,level+1)
                    print("    "*(level+1)+"*")
            else:
                self._printTree(root.left,level+1)
                self._printTree(root.right,level+1)
    

avl_tree = AVL_Tree()
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        avl_tree.insert(data)
    elif op == "D":
        avl_tree.delete(data)
    elif op == "P":
        avl_tree.printTree()
        print("------------------------------")
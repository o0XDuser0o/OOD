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

    def _insert(self,data,root: Node):
        if root == None:
            root = Node(data)
        elif data < root.data:
            root.left = self._insert(data,root.left)
        else:
            root.right = self._insert(data,root.right)
        return root
    def printtree(self):
        self._printTree(self.root)

    def _printTree(self, node: Node, level = 0):
        if node != None:
            self._printTree(node.right, level + 1)
            print('     ' * level, node)
            self._printTree(node.left, level + 1)
    
    def ranking(self,data):
        return self._ranking(data,self.root)

    def _ranking(self,data,root: Node,rank = 0):
        if root == None:
            return rank
        rank = self._ranking(data,root.left,rank)
        if root.data <= data:
            rank += 1
        rank = self._ranking(data,root.right,rank)
        return rank

t = BST()
d,n = input("Enter Input : ").split("/")
for i in list(map(int,d.split(" "))):
    t.insert(i)
t.printtree()
print("--------------------------------------------------")
print("Rank of",n,":",t.ranking(int(n)))
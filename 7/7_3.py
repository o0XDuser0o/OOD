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
        q = []
        h = data.pop(0)
        self.root = h
        q.append(h)
        while q:
            if not data:
                break
            if q[0].left == None:
                lf = data.pop(0)
                q[0].left = lf
                q.append(lf)
            elif q[0].right == None:
                rt = data.pop(0)
                q[0].right = rt
                q.append(rt)
                q.pop(0)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findmost(self,root):
        if root == None:
            return []
        ll = self.findmost(root.left)
        rl = self.findmost(root.right)
        if sum(rl) >= sum(ll):
            return [root.data] + rl
        return [root.data] + ll

l = list(map(Node,map(int,input("Enter tree: ").split(" "))))
t = BST()
t.insert(l)
print("Maximum path:",t.findmost(t.root))


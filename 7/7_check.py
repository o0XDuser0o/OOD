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

    def _insert(self,data,root : Node):
        if root == None:
            root = Node(data)
        elif data < root.data:
            root.left = self._insert(data,root.left)
        else:
            root.right = self._insert(data,root.right)
        return root
    def printtree(self):
        txt,ms,ls,rs =  self._printtree(self.root)
        print(*txt, sep="\n")

    def _printtree(self, root: Node):
        if root == None:
            return [], 0, 0, 0
        ms = len(str(root.data))
        if root.left is None and root.right is None:
            return [str(root.data)], ms, 0, 0

        ltxt, lms, lls, lrs = self._printtree(root.left)
        rtxt, rms, rls, rrs = self._printtree(root.right)
        lslash = int(bool(lms))
        rslash = int(bool(rms)) 
        txt = [" "*(lms+lls+lrs+lslash) + str(root.data) + " "*(rms+rls+rrs+rslash),
                " "*(lms+lls) + "_"*lrs + "/"*lslash + " "*ms + "\\"*rslash + "_"*rls + " "*(rms+rrs)]

        if len(rtxt) > len(ltxt):
            ltxt += [" " * (lms+lls+lrs)] * (len(rtxt)-len(ltxt))
        elif len(rtxt) < len(ltxt):
            rtxt += [" " * (rms+rls+rrs)] * (len(ltxt)-len(rtxt))

        for l, r in zip(ltxt, rtxt):
            txt.append(l + " "*(ms+lslash+rslash) + r)
        
        return txt, ms, lms+lls+lrs+lslash, rms+rls+rrs+rslash
    
    def findroot(self,data):
        if self.root.data == data:
            return "Root"
        return self._findroot(data,self.root)
        
    def _findroot(self,data,root : Node):
        if root == None:
            return "Not exist"
        elif data < root.data:
            return self._findroot(data,root.left)
        elif data > root.data:
            return self._findroot(data,root.right)
        else:
            if root.left == None and root.right == None:
                return "Leaf"
            return "Inner"
    
t = BST()
inp = list(map(int,input("Enter Input : ").split(" ")))
print(inp)
for i in range(1,len(inp)):
    t.insert(inp[i])
t.printtree()
print(t.findroot(inp[0]))
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
            print("*")
        elif data < root.data:
            print("L",end="")
            root.left = self._insert(data,root.left)
        else:
            print("R",end="")
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
    
t = BST()
for i in list(map(int,input("Enter Input : ").split(" "))):
    t.insert(i)
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
    
    def findpower(self,index):
        n,c = self._findnode(index,0,self.root)
        return self._findpower(n,0)

    def _findpower(self,root: Node,p):
        if root == None:
            return p
        p = self._findpower(root.left,p)
        p += root.data
        p = self._findpower(root.right,p)
        return p

    def _findnode(self,findex,index,root: Node):
        if root == None:
            return None,False
        if findex == index:
            return root,True
        node,checker = self._findnode(findex,index*2+1,root.left)
        if not checker:
            node,checker = self._findnode(findex,index*2+2,root.right)
        return node,checker

t = BST()
knight,cpower = input("Enter Input : ").split("/")
t.insert(list(map(Node,map(int,knight.split()))))
print(t.findpower(0))
for act in cpower.split(","):
    a,b = act.split()
    a,b = int(a),int(b)
    if t.findpower(a)>t.findpower(b):
        print(f'{a}>{b}')
    elif t.findpower(a)<t.findpower(b):
        print(f'{a}<{b}')
    else:
        print(f'{a}={b}')
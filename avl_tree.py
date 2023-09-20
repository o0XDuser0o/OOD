from binary_tree import BST

class AVLTree(BST):
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        
        def __str__(self):
            return str(self.data)
        
        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a,b)
                return self.height
            
        def getHeight(self, node):
            return -1 if node == None else node.height
            
        def balanceValue(self):
            return self.getHeight(self.left) - self.getHeight(self.right)
    
    def __init__(self, root = None):
        self.root = None if root is None else root
    
    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root is None:
            return self.AVLNode(data)
        else:
            if int(data) < int(root.data):
                root.left = self._add(root.left, data)
            else:
                root.right = self._add(root.right, data)
            root = self.rebalanceS(root)                
            return root
    
    def rebalanceS(self, x):
        if x == None:
            return x
        balance = x.balanceValue()
        if balance == -2 : 
            if x.right.balanceValue() == 1 :
                x.right = self.leftRotage(x.right)
            x = self.rightRotage(x)
        elif balance == 2 : 
            if x.left.balanceValue() == -1:   
                x.left = self.rightRotage(x.left)                                         
            x = self.leftRotage(x)
        x.setHeight()
        return x 
  
    def leftRotage(self, x) :
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        x.right.setHeight()
        x.setHeight()
        return x
    
    def rightRotage(self, x) :
        y = x.right
        x.right = y.left
        y.left = x    
        x = y
        x.left.setHeight()
        x.setHeight()
        return x
     
        
    def __str__(self) -> str:
        lines = AVLTree._build_tree_string(self.root, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def _build_tree_string(
        root: AVLNode,
        curr_index: int,
        include_index: bool = False,
        delimiter: str = "-") :

        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        if include_index:
            node_repr = "{}{}{}".format(curr_index, delimiter, root.data)
        else:
            node_repr = str(root.data) + ":" + str(root.height) ## add for other value to display

        new_root_width = gap_size = len(node_repr)

        l_box, l_box_width, l_root_start, l_root_end = AVLTree._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = AVLTree._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(" " * (l_root + 1))
            line1.append("_" * (l_box_width - l_root))
            line2.append(" " * l_root + "/")
            line2.append(" " * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        else:
            new_root_start = 0

        line1.append(node_repr)
        line2.append(" " * new_root_width)

        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append("_" * r_root)
            line1.append(" " * (r_box_width - r_root + 1))
            line2.append(" " * r_root + "\\")
            line2.append(" " * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        gap = " " * gap_size
        new_box = ["".join(line1), "".join(line2)]
        for i in range(max(len(l_box), len(r_box))):
            l_line = l_box[i] if i < len(l_box) else " " * l_box_width
            r_line = r_box[i] if i < len(r_box) else " " * r_box_width
            new_box.append(l_line + gap + r_line)

        return new_box, len(new_box[0]), new_root_start, new_root_end

    def inOrder(self):
        print("AVLTree in-order : ",end="")
        self._inOrder(self.root)
        print()
            
    def _inOrder(self, root):
        if root is not None:
            self._inOrder(root.left)
            print(root, end = ' ')
            self._inOrder(root.right) 
    
    def postOrder(self):
        print("AVLTree post-order : ",end="")
        self._postOrder(self.root)
        print()
            
    def _postOrder(self, root):
        if root is not None:
            self._postOrder(root.left)
            self._postOrder(root.right)
            print(root, end = ' ')
    
    def delete(self, data) :
        self.root = self._delete(self.root, data)
  
    def _delete(self, root, key) :
        if root is None : return root
        if int(key) < int(root.data) :
            root.left = self._delete(root.left, key)
        elif int(key) > int(root.data) :
            root.right = self._delete(root.right, key)
        else :
            if root.left is None or root.right is None :
                root = root.left if root.right is None else root.right
            else :
                temp = root.left
                while temp.right is not None :
                    temp = temp.right
                root.data = temp.data
                root.left = self._delete(root.left, temp.data)
            root = self.rebalanceS(root)         
        return root
  

avl1 = AVLTree()
avl1.add(1)
print(avl1)
avl1.add(2)
print(avl1)
avl1.add(3)
print(avl1)
avl1.add(6)
print(avl1)
avl1.add(8)
print(avl1)
avl1.add(4)
print(avl1)
avl1.add(15)
print(avl1)
avl1.add(14)
print(avl1)

avl1.delete(3)
print(avl1)
avl1.delete(14)
print(avl1)
# avl1.postOrder()
# avl1.inOrder()
# avl1.postOrder()
# avl1.leverOrder()



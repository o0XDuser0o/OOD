#AJ's code

class Queue:
    def __init__(self, q = None):
        if q == None:
            self.item = []
        else:
            self.item = q
    def enQueue(self, i):
        self.item.append(i)
    def deQueue(self):
        return self.item.pop(0)
    def isEmpty(self):
        return self.item == []
    def size(self):
        return len(self.item)

class BST:
    class Node:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
        
        def __str__(self):
            s = str(self.data)
            return s
    
    def __init__(self, root = None):
        self.root = None if root is None else root
        
    def add(self, data):
        self.root = BST._add(self.root, data)
        

    def _add(root, data):
        if root is None:
            return BST.Node(data)
        else:
            if data < root.data:
                root.left = BST._add(root.left, data)
            else:
                root.right = BST._add(root.right, data)
        return root
    
    def leverOrder(self):
        q = Queue()
        q.enQueue(self.root)
        while q.isEmpty() is not True :
            n = q.deQueue()
            print(n.data, end = ' ')
            if n.left is not None:
                q.enQueue(n.left)
            if n.right is not None:
                q.enQueue(n.right)
        

    def inOrder(self):
        BST._inOrder(self.root)

    def _inOrder(root):
        if root is not None:
            BST._inOrder(root.left)
            print(root, end = ' ')
            BST._inOrder(root.right)
    
    def preOrder(self):
        BST._preOrder(self.root)

    def _preOrder(root):
        if root is not None:
            print(root, end = ' ') 
            BST._preOrder(root.left)
            BST._preOrder(root.right)

    def postOrder(self):
        BST._postOrder(self.root)

    def _postOrder(root):
        if root is not None:
            BST._postOrder(root.left)
            BST._postOrder(root.right)
            print(root, end = ' ')


    def deleteNode(self, data):
        self.root = BST._deleteNodeP(self.root, data)
        
    def _deleteNodeS(root : Node, key : int) :
        if root is None : return root
        if int(key) < int(root.data) :
            root.left = BST._deleteNodeS(root.left, key)
        elif int(key) > int(root.data) :
            root.right = BST._deleteNodeS(root.right, key)
        else :
            if root.left is None or root.right is None :
                root = root.left if root.right is None else root.right
            else :
                temp = root.right
                while temp.left is not None :
                    temp = temp.left
                root.data = temp.data
                root.right = BST._deleteNodeS(root.right, temp.data)
        return root  

    def _deleteNodeP(root : Node, key : int) :
        if root is None:
            print("Error! Not Found DATA") 
            return root
        if int(key) < int(root.data) :
            root.left = BST._deleteNodeP(root.left, key)
        elif int(key) > int(root.data) :
            root.right = BST._deleteNodeP(root.right, key)
        else :
            if root.left is None or root.right is None :
                root = root.left if root.right is None else root.right
            else :
                temp = root.left
                while temp.right is not None :
                    temp = temp.right
                root.data = temp.data
                print(f'p = {root.data}')
                root.left = BST._deleteNodeP(root.left, temp.data)
        return root  

    def __str__(self) -> str:
        lines = BST._build_tree_string(self.root, 0, False, "-")[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))
    
    def _build_tree_string( 
        root: Node,
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
            node_repr = str(root.data)
        new_root_width = gap_size = len(node_repr)
        l_box, l_box_width, l_root_start, l_root_end = \
            BST._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = \
            BST._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)
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
    
    
tree1 = BST()
tree1.add(30)
tree1.add(40)
tree1.add(21)
tree1.add(43)
tree1.add(32)
tree1.add(14)
tree1.add(25)
tree1.add(18)
tree1.add(12)
tree1.add(28) 
tree1.add(22)
tree1.add(29)
# tree1.add(19)
# tree1.add(13)
print(tree1)

tree1.deleteNode(21)
print(tree1)
#print("Lever order : ",end="")
#tree1.leverOrder()
#print()
#print("Inorder : ",end="")
#tree1.inOrder()
#print()
# print("Post order : ",end="")
# tree1.postOrder()
# print()
# print("Pre order : ",end="")
# tree1.preOrder()
# print()



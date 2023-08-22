class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
    
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def size(self):
        if self.isEmpty():
            return 0
        n = self.head
        i = 1
        while n.next != None:
            n = n.next
            i += 1
        return i

    def append(self,item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
    
    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head = n
    
    def insert(self,item,pos):
        insert_n = Node(item)
        i = 1
        if pos < 0:
            pos = self.size() + pos
        if self.isEmpty():
            self.head = self.tail = insert_n
        elif pos <= 0:
            self.addHead(item)
        elif pos >= self.size():
            self.append(item)
        else:
            n = self.head
            while n.next != None and i < pos:
                n = n.next
                i += 1
            insert_n.next = n.next
            n.next = insert_n

    def pop(self,pos):
        i = 0
        if pos < 0:
            pos = self.size() + pos
        if pos >= self.size() or pos < 0:
            raise Exception("Out of Range")
        elif pos == 0:
            self.head = self.head.next
        else:
            n = self.head
            while n.next != None and i < pos-1:
                n = n.next
                i += 1
            if pos == self.size() - 1:
                self.tail = n
                self.tail.next = None
            else:
                n.next = n.next.next
    
    def index(self, pos):
        if self.isEmpty():
            raise Exception("Empty")
        n = self.head
        i = 0
        while i < pos:
            n = n.next
            i+=1
        return n.value

def createLL(LL):
    sll = LinkedList()
    for i in LL:
        sll.append(i)
    return sll

def printLL(head):
    return str(head)

def SIZE(head):
    return head.size()

def bottomUp(head,b):
    for i in range(b):
        item = head.head.value
        head.pop(0)
        head.append(item)

def de_bottomUp(head,b):
    for i in range(b):
        item = head.tail.value
        head.pop(-1)
        head.addHead(item)

def riffleShuffle(head,r): #fix
    linkedlist = LinkedList()
    for i in range(head.size()-r):
        linkedlist.addHead(head.tail.value)
        head.pop(-1)
    for i in range(linkedlist.size()):
        head.insert(linkedlist.head.value,2*i+1)
        linkedlist.pop(0)
    

def de_riffleShuffle(head,r):
    linkedlist = LinkedList()
    if r <= head.size() - r:
        for i in range(r):
            linkedlist.append(head.index(i))
            head.pop(i)
        for i in range(linkedlist.size()):
            head.addHead(linkedlist.tail.value)
            linkedlist.pop(-1)
    else:
        for i in range(head.size() - r):
            linkedlist.append(head.index(i+1))
            head.pop(i+1)
        for i in range(linkedlist.size()):
            head.append(linkedlist.head.value)
            linkedlist.pop(0)

def scarmble(head, b, r, size):
    bea = int((b/100)*size)
    rea = int((r/100)*size)
    bottomUp(head,bea)
    print("BottomUp {:.3f} % :".format(b),head)
    riffleShuffle(head,rea)
    print("Riffle {:.3f} % :".format(r),head)
    de_riffleShuffle(head,rea)
    print("Deriffle {:.3f} % :".format(r),head)
    de_bottomUp(head,bea)
    print("Debottomup {:.3f} % :".format(b),head)

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)


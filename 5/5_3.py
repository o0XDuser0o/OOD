class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        for i in range(self.size()-1):
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None
    
    def isCircular(self):
        return self.head == self.tail and not self.isEmpty()
    
    def makeCircular(self):
        self.tail.next = self.head
        self.tail = self.head
    
    def size(self):
        if self.isEmpty():
            return 0
        n = self.head
        i = 1
        while n.next != None and n.next != self.head:
            n = n.next
            i += 1
        return i
    
    def append(self,item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
            return
        self.tail.next = n
        self.tail = n

    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
            return
        n.next = self.head
        self.head = n

    def pop(self,pos):
        pass

    def search(self, item):
        if self.isEmpty():
            return False
        n = self.head
        for i in range(self.size()):
            if n.value == item:
                return True
            n = n.next
        return False

inp = [[int(i) for i in act.split(">")] for act in input("Enter edges: ").split(",")]
loll = []
dump = []

for i in inp: #first scan
    for ll in loll:
        if ll.search(i[0]):
            if ll.tail.value == i[0] and ll.head.value == i[1]:
                ll.makeCircular()
                break
            elif ll.tail.value == i[0]: 
                ll.append(i[1])
                break
            elif i[0] not in dump:
                dump.append(i[0])

        elif ll.search(i[1]):
            if ll.head.value == i[1]:
                ll.addHead(i[0])
                break
            elif i[1] not in dump:
                dump.append(i[1])

    else:
        loll.append(SLinkedList())
        if i[0] == i[1]:
            loll[-1].append(i[0])
            loll[-1].makeCircular()
        else:
            loll[-1].append(i[0])
            loll[-1].append(i[1])

for ll in loll: #second scan
    if not ll.isCircular():
        for ell in loll:
            if ll != ell and not ell.isCircular() and ll.tail.value == ell.head.value:
                ll.tail.next = ell.head.next
                ll.tail = ell.tail
                loll.remove(ell)
                if ll.head.value == ll.tail.value:
                    ll.tail.next = ll.head.next
                    ll.tail = ll.head = ll.tail.next

dump.sort()
if dump == []:
    print("No intersection")
    exit()

for num in dump: #intersect displayer
    num_list = []
    for ll in loll:
        if ll.search(num):
            checker = False
            n = ll.head
            while n != None and (not checker or n.value != num):
                if n.value == num:
                    checker = True
                if checker and n.value not in num_list:
                    num_list.append(n.value)
                n = n.next
                
        elif ll.head.value in num_list:
            n = ll.head.next
            for i in range(ll.size()-1):
                num_list.append(n.value)
    print("Node({}, size={})".format(num,len(num_list)))
print("Delete intersection then swap merge:")

swap = [] #intersect filter
for ll in loll:
    for num in dump:
        if ll.search(num) and ll not in swap or not ll.isCircular():
            swap.append(ll)
            break

head = [] #intersect destroyer
for ll in swap: 
    n = ll.head
    while n.value in dump:
        n = n.next
    head.append(n)
    while n.next != None:
        if n.next.value in dump:
            newn = n.next.next
            while newn != None and newn.value in dump:
                newn = newn.next
            n.next = None
            if newn == None or newn == n:
                break
            head.append(newn)
            n = newn
        else:
            n = n.next

for node in head: #head filter
    for cnode in head:
        if node != cnode:
            n = cnode
            while n != None:
                if node.value == n.value:
                    head.remove(node)
                    break
                n = n.next

sortlist = [] #sorter
sorthead = []
for node in head:
    sortlist.append(node.value)
sortlist.sort()
for num in sortlist:
    for node in head:
        if num == node.value:
            sorthead.append(node)
            break

stxt = [] #swaper
while len(sorthead) != 0:
    txt = []
    size = len(sorthead)
    for i in range(size):
        x = sorthead.pop(0)
        txt.append(x.value)
        if x.next != None:
            sorthead.append(x.next)
    for i in txt:
        stxt.append(str(i))

print(" -> ".join(stxt))


    









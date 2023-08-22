class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
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

    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.previous = self.tail
            self.tail.next = n
            self.tail = n

    def addHead(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head.previous = n
            self.head = n

    def search(self, item):
        if self.isEmpty():
            return "Not Found"
        n = self.head
        while n.next != None:
            if n.value == item:
                return "Found"
            n = n.next
        if n.value == item:
                return "Found"
        return "Not Found"

    def index(self, item):
        if self.isEmpty():
            return -1
        n = self.head
        i = 0
        while n.next != None:
            if n.value == item:
                return i
            n = n.next
            i+=1
        if n.value == item:
                return i
        return -1

    def insert(self, pos, item):
        i = 1
        insert_n = Node(item)
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
            insert_n.previous = n
            n.next.previous = insert_n
            n.next = insert_n
        return

    def pop(self, pos):
        i = 0
        if pos < 0:
                pos = self.size() + pos
        if pos >= self.size() or pos < 0:
            return "Out of Range"
        elif pos == 0:
            self.head = self.head.next
            if self.head != None:
                self.head.previous = None
        elif pos == self.size() - 1:
            self.tail = self.tail.previous
            if self.tail != None:
                self.tail.next = None
        else:
            n = self.head
            while n.next != None and i < pos:
                n = n.next
                i += 1
            n.next.previous = n.previous
            n.previous.next = n.next
        return "Success"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
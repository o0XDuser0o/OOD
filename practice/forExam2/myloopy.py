class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def isCircular(self):
        if self.isEmpty():
            return False
        n = self.head
        if n == n.next:
            return True
        while n.next != None:
            if n.next == self.head:
                return True
            n = n.next
        return False

    def size(self):
        if self.isEmpty():
            return 0
        i,n = 1,self.head
        if self.isCircular():
            while n.next != self.head:
                i += 1
                n = n.next
            return i
        while n.next != None:
            i += 1
            n = n.next
        return i
    

    def append(self,data):
        n = Node(data)
        if self.isEmpty():
            self.head = self.tail = n
            return
        if self.isCircular():
            n.next = self.head.next
            self.head.next = n
            self.head = self.tail = n
            return
        self.tail.next = n
        self.tail = n

    def findNode(self,index):
        if index >= self.size():
            return 0
        n = self.head
        if self.isCircular():
            n = self.head.next
        for i  in range(self.size()):
            if i == index:
                return n
            n = n.next

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        if self.isCircular():
            txt,n = str(self.head.next.data)+"->",self.head.next
            while n != self.head:
                n = n.next
                txt = txt + str(n.data) + "->"
            return txt[:-2]
        txt,n = str(self.head.data)+"->",self.head
        while n.next != None:
            n = n.next
            txt = txt + str(n.data) + "->"
        return txt[:-2]

ll = LinkedList()
for act in input("Enter input : ").split(","):
    if act[:1] == "A":
        ll.append(act[2:])
        print(ll)
    if act[:1] == "S":
        start,finish = map(int,act[2:].split(":"))
        if ll.isEmpty():
            print('Error! {list is empty}')
        elif finish >= ll.size() and start < ll.size():
            print('index not in length, append :',finish)
            ll.append(finish)
        elif start >= ll.size():
            print('Error! {index not in length}:',start)
        else:
            s = ll.findNode(start)
            f = ll.findNode(finish)
            s.next = f
            if start >= finish:
                ll.head = ll.tail = s
            print(f'Set node.next complete!, index:value = {start}:{s.data} -> {finish}:{f.data}')

if ll.isCircular():
    print("loop")
else:
    print("no loop")    
print(ll)
        
class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None
 
class Linkedlist: #not good enough
    def __init__(self) -> None:
        self.head = self.tail = self.ptr = None

    def size(self):
        if self.head == None:
            return 0
        n = self.head
        i = 1
        while n.next != None:
            n = n.next
            i += 1
        return i
    
    def isEmpty(self):
        return self.size() == 0
    
    def append(self,data):
        n =Node(data)
        if self.isEmpty():
            self.head = self.tail = self.ptr = n
            return
        if self.ptr == self.tail:
            self.tail.next = n
            n.prev = self.tail
            self.tail = self.ptr = n
            return
        if self.ptr == None:
            self.head.prev = n
            n.next = self.head
            self.head = self.ptr = n
            return
        n.next = self.ptr.next
        self.ptr.next.prev = n
        n.prev = self.ptr
        self.ptr.next = n
        self.ptr = n

    def backpath(self):
        if self.isEmpty():
            raise Exception("Empty")
        self.ptr = self.ptr.prev
        return self.ptr.data

    def forpath(self):
        if self.isEmpty():
            raise Exception("Empty")
        self.ptr = self.ptr.next
        return self.ptr.data

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        txt,n = self.head.data+" ->",self.head
        while n.next != None:
            n = n.next
            txt = txt + n.data + " ->"
        return txt[:-2]
    
    def reverse(self):
        if self.isEmpty():
            return "Empty"
        txt,n = self.ptr.data+" ->",self.ptr
        while n.prev != None:
            n = n.prev
            txt = txt + n.data + " ->"
        return txt[:-2]

history = Linkedlist()
path = Linkedlist()
for web in input("Enter Input : ").split(","):
    if web[:1] == "E":
        history.append(web[2:])
        path.append(web[2:])
    elif web[:1] == "B":
        history.append(path.backpath())
    elif web[:1] == "F":
        history.append(path.forpath())

print(f'History : {history}')
print(f'BackPath : {path.reverse()}')
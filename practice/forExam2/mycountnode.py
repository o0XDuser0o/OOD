class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = self.tail = None

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
            self.head = self.tail = n
            return
        self.tail.next = n
        self.tail = n

    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        txt,n = self.head.data+" ",self.head
        while n.next != None:
            n = n.next
            txt = txt + n.data + " "
        return txt
    
    def count(self,k):
        if k > self.size():
            print("Over length")
            return
        n,i = self.head,0
        while n != None:
            if i%k == 0 and n.next != None:
                print(f'Now index {i} value is {n.data} next value is {n.next.data}')
            elif i%k == 0:
                print(f'Now index {i} value is {n.data} next value is -1')
            i += 1
            n = n.next
                



items,k = input("Input : ").split("/")
ll = Linkedlist()
for item in items.split(" "):
    ll.append(item)
ll.count(int(k))


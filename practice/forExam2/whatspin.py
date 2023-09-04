class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:
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

    def spin(self,k,start = None):
        if self.isEmpty():
            return None
        i = 0
        if start == None:
            start = self.head
        n = start
        pn = None
        nn = None
        while n != None and i < k:
            nn = n.next
            n.next = pn
            pn = n
            n = nn
            i += 1
        if n != None:
            start.next = self.spin(k,n)
        return pn

    def retail(self):
        n = self.head
        while n.next != None:
            n = n.next
        self.tail = n
    
    def __str__(self) -> str:
        if self.isEmpty():
            return "Empty"
        arrow = " <-> "
        if self.head.data.isalpha():
            arrow = " > "
        txt,n = self.head.data+arrow,self.head
        while n.next != None:
            n = n.next
            txt = txt + n.data + arrow
        if arrow == " > ":
            return txt[:-3]
        return txt[:-5]
        

ll = LinkedList()
l,k = input("Enter the elements of Linked list/group's size: ").split("/")
if ll == "":
    print("No elements in Linked List ? OK!")
elif int(k) <= 0:
    print( "Group' size should be greater than 0")
else:
    for data in l.split(" "):
        ll.append(data)
    print("")
    print("Original Linked list:",ll)
    ll.head = ll.spin(int(k),ll.head)
    ll.retail()
    print("Modified Linked list: ",ll)
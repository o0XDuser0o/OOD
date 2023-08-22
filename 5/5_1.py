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
        for i in range(self.size()-1):
            s += str(cur.next.value) + " "
            cur = cur.next
        return s
    
    def size(self):
        if self.isEmpty():
            return 0
        n = self.head
        i = 1
        while n.next != None and n.next != self.head:
            n = n.next
            i += 1
        return i
    
    def isEmpty(self):
        return self.head == None

    def isCircular(self):
        return self.head == self.tail and not self.isEmpty()
    
    def makeCircular(self):
        self.tail.next = self.head
        self.head.previous = self.tail
        self.tail = self.head

    def append(self, item):
        n = Node(item)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.previous = self.tail
            self.tail.next = n
            self.tail = n
    
    def forward(self,ori,des):
        n = self.head
        for i in range(self.size()):
            if n.value == ori:
                break
            n = n.next
        station = [n.value]
        while n.next.value != des:
            n = n.next
            station.append(n.value)
        station.append(n.next.value)
        return station,len(station)-1

    def backward(self,ori,des):
        n = self.head
        for i in range(self.size()):
            if n.value == ori:
                break
            n = n.next
        station = [n.value]
        while n.previous.value != des:
            n = n.previous
            station.append(n.value)
        station.append(n.previous.value)
        return station,len(station)-1


print("***Railway on route***")
sta,trav = input("Input Station name/Source, Destination, Direction(optional): ").split("/")
stall = LinkedList()
action = [act for act in trav.split(",")]
for station in sta.split(","):
    stall.append(station)
stall.makeCircular()

if len(action) == 3:
    if action[2] == "F":
        s,i = stall.forward(action[0],action[1])
        print("Forward Route: {},{}".format("->".join(s),i))
    else:
        s,i = stall.backward(action[0],action[1])
        print("Backward Route: {},{}".format("->".join(s),i))
else:
    fs,fi = stall.forward(action[0],action[1])
    bs,bi = stall.backward(action[0],action[1])
    if bi > fi:
        print("Forward Route: {},{}".format("->".join(fs),fi))

    elif bi< fi:
        print("Backward Route: {},{}".format("->".join(bs),bi))
    else:
        print("Forward Route: {},{}".format("->".join(fs),fi))
        print("Backward Route: {},{}".format("->".join(bs),bi))
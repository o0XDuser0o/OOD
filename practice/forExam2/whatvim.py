class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
    
    def size(self):
        s = 0
        temp = self.head
        while temp != None:
            s += 1
            temp = temp.next
        return s
    
    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.isEmpty() == True:
            return 'Empty'
        temp, s = self.head, str(self.head.data) + " "
        while temp.next != None:
            s += str(temp.next.data) + ' '
            temp = temp.next
        
        return s
    
    def addHead(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        newNode.next = self.head
        self.head.previous = newNode
        self.head = newNode
    
    def pop(self, pos):
        lenght = self.size()
        if not (-lenght < pos < lenght):
            print("POP: OUT OF RANGE")
        p = -lenght
        temp = self.head
        while p != pos:
            p += 1
            temp = temp.next
            if temp == None:
                temp = self.head
        
        if temp == self.head:
            self.head = self.head.next
            temp.next = None
            if self.head != None:
                self.head.previous = None
            return 'Remove Head'

        elif temp == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
            return 'Remove TAIL'

        else:
            temp.next.previous = temp.previous
            temp.previous.next = temp.next
    
    def insert(self, data, pos):
        lenght = self.size()
        if pos <= 0:
            self.addHead(data)
            return
        if pos >= lenght:
            self.append(data)
            return
        
        newNode = Node(data)
        p = 0
        temp = self.head
        while p != pos:
            p += 1
            temp = temp.next
        
        newNode.next = temp
        newNode.previous = temp.previous
        temp.previous.next = newNode
        temp.previous = newNode


inputstr = input("Enter Input : ").split(',')

ll = LinkedList()
ll.append('|')
pos = 0
for i in inputstr:
    action = i.split()[0]
    print(action)

    if action == 'L':
        if pos >= 1 and ll.size() > 1:
            ll.pop(pos)
            ll.insert('|', pos-1)
            pos -= 1
            print(f"pos {pos} {ll}")

    elif action == 'R' and ll.size() > 1:
        if pos < ll.size() and pos != ll.size() - 1:
            ll.pop(pos)
            ll.insert('|', pos+1 )
            pos += 1
            print(f"pos {pos} {ll}")
    
    elif action == 'B':
        if pos != 0:
            ll.pop(pos-1)
            print(f"pos {pos} {ll}")
            pos -= 1

    elif action == 'D':
        print(f"before delete {ll}")
        if pos != ll.size() - 1:
            ll.pop(pos+1)
            print(f"pos {pos} {ll}")


    if action == 'I':
        ll.pop(pos)
        ll.insert(i.split()[1], pos)
        pos += 1
        ll.insert('|', pos)
        print(f"append: {ll}")

print(ll)
#print(pos)
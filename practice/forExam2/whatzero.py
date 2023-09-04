class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
            self.tail = temp
        
        else:
            self.tail.next = temp
            self.tail = temp

    def __str__(self):
        temp = self.head
        stri = ''
        while temp is not None:
            stri += str(temp.data)
            if temp.next != None:
                stri += " <- "
            temp = temp.next

        return str(stri)

    def sol(self):
        oldhead = self.head
        temp = self.head
        while temp != None:
            if temp.data == 0:
                newhead = temp
                break
            temp = temp.next

        self.head = newhead
        temp = self.head
        while temp != None:
            if temp.next == None:
                temp.next = oldhead
            elif temp.next.data == 0:
                temp.next = None
            temp = temp.next
            
        
print(" *** Locomotive ***")
inputstr = list(map(int,input("Enter Input : ").split()))

print("Before : ",end = "")
print(*inputstr, sep=" <- ")

ll = Linkedlist()
for i in inputstr:
    ll.append(i)
ll.sol()
print(f"After : {ll}")
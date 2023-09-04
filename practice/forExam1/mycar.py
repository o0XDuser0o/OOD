class Stack:
    def __init__(self,items = None):
        if items == None:
            self.stack = []
        else:
            self.stack = items
    
    def size(self):
        return len(self.stack)
    
    def isEmpty(self):
        return self.size() == 0
    
    def push(self,item):
        return self.stack.append(item)
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Cannot pop empty stack")
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Cannot peek empty stack")
        return self.stack[-1]
    
    def __str__(self) -> str:
        return str(self.stack)

print("******** Parking Lot ********")
m,s,o,n = input("Enter max of car,car in soi,operation : ").split()
m,n = int(m),int(n)
soi = Stack()
road = Stack()
if s != "0":
    for car in s.split(","):
        soi.push(int(car))

if o == 'arrive':
    if soi.size() == m:
        print("full")
        exit()
    else:
        while not soi.isEmpty():
            a = soi.pop()
            if a == n:
                print("already in")
                exit()
            road.push(a)
        while not road.isEmpty():
            soi.push(road.pop())
        soi.push(n)
        print(soi)
else:
    if soi.size() == 0:
        print("empty")
    else:
        while not soi.isEmpty():
            a =soi.pop()
            if a != n:
                road.push(a)
        while not road.isEmpty():
            soi.push(road.pop())
        print(soi)
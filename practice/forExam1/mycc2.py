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
    
class Queue:
    def __init__(self,items = None):
        if items == None:
            self.queue = []
        else:
            self.queue[items]
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enQueue(self,item):
        return self.queue.append(item)
    
    def deQueue(self):
        if self.isEmpty():
            raise Exception("Cannot dequeue empty stack")
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            raise Exception("Cannot front empty stack")
        return self.queue[0]
    
    def rear(self):
        if self.isEmpty():
            raise Exception("Cannot rear empty stack")
        return self.queue[-1]
    
    def __str__(self):
        return str(self.queue)
    
nor,mir = input("Enter Input (Normal, Mirror) : ").split(" ")
mirs = Stack()
nors = Stack()
ob = Queue()
mir_com = 0
nor_com = 0
mistake = 0
for char in reversed(mir):
    if mirs.size() >= 2:
        a = mirs.pop()
        b = mirs.pop()
        if a == b and b == char:
            mir_com += 1
            ob.enQueue(char)
        else:
            mirs.push(b)
            mirs.push(a)
            mirs.push(char)
    else:
        mirs.push(char)

for char in nor:
    if nors.size() >= 2:
        a = nors.pop()
        b = nors.pop()
        if a == b and b == char and not ob.isEmpty():
            c = ob.deQueue()
            if a == c and c == char:
                mistake += 1
                nors.push(b)
            else:
                nors.push(b)
                nors.push(a)
                nors.push(c)
                nors.push(char)
        elif a == b and b == char:
            nor_com += 1
        else:
            nors.push(b)
            nors.push(a)
            nors.push(char)
    else:
        nors.push(char)

print(nors,nor_com)
print(mirs,mir_com)
print(mistake)


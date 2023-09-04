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

inp = []    
s = Stack()
for x in input("Enter Input : ").split(","):
    w,f = x.split(" ")
    inp.append([w,f])

for plate in inp:
    if s.isEmpty():
        s.push(plate)
    else:
        while not s.isEmpty() and s.peek()[0] < plate[0]:
            print(s.pop()[1])
        s.push(plate)
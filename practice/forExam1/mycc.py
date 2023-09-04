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

s = Stack()
combo = 0    
x = [char for char in input("Enter Input : ").split(" ")]
for char in x:
    if s.size() >= 2:
        a = s.pop()
        b = s.pop()
        print(a,b,char)
        if a == b and b == char:
            
            combo +=1
        else:
            s.push(b)
            s.push(a)
            s.push(char)
    else:
        s.push(char)

print(s.size())
while not s.isEmpty():
    print(s.pop(),end="")
print("\nCombo :",combo,"! ! !")
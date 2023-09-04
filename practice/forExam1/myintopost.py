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
    
prio = {
    "^": 10,
    "*":8,
    "/":8,
    "+":6,
    "-":6
}
operator = Stack()
result = ""

for char in input("Enter input : "):
    if char == "(":
        operator.push(char)
    elif char == ")":
        while operator.peek() != "(":
            result  = result +  operator.pop()
        operator.pop()
    elif char in "^*/+-":
        while not operator.isEmpty() and operator.peek() != "(" and prio[operator.peek()] >= prio[char]:
            result  = result +  operator.pop()
        operator.push(char)
    else:
        result = result + char

while not operator.isEmpty():
    result  = result +  operator.pop()

print(result)

    
class stack:
    def __init__(self):
        self.__index = []

    def __len__(self):
        return len(self.__index)

    def push(self,item):
        self.__index.insert(0,item)

    def peek(self):
        if len(self) == 0:
            raise Exception("peek() called on empty stack.")
        return self.__index[0]

    def pop(self):
        if len(self) == 0:
            raise Exception("pop() called on empty stack.")
        return self.__index.pop(0)

    def __str__(self):
        return ''.join(self.__index)

operator = stack()
result = ""
x = [char for char in input("Enter Infix : ")]
for i in range(len(x)):
    if x[i] not in "+-*/^()":
        result += x[i]
    elif x[i] == "(":
        operator.push(x[i])
    elif x[i] == ")":
        while len(operator) > 0 and operator.peek() != "(":
            result += operator.pop()
        operator.pop()
    elif x[i] == "^":
        operator.push(x[i])
    elif x[i] in "*/":
        while len(operator) > 0 and operator.peek() in "^/*":
            result += operator.pop()
        operator.push(x[i])
    elif x[i] in "+-":
        while len(operator) > 0 and operator.peek() in "^*/+-":
            result += operator.pop()
        operator.push(x[i])
while len(operator) > 0:
    result += operator.pop()
print("Postfix :",result)
    



    
    

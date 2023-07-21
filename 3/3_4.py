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
        return str(self.__index)

print("* Stack Calculator *")
x = [w for w in input("Enter arguments : ").split(" ")]
result = stack()
for i in x:
    if i == "DUP":
        result.push(result.peek())
    elif i == "POP":
        result.pop()
    elif i.isnumeric():
        result.push(int(i))
    elif i == "+":
        x = result.pop()
        y = result.pop()
        result.push(x + y)
    elif i == "-":
        x = result.pop()
        y = result.pop()
        result.push(x - y)
    elif i == "*":
        x = result.pop()
        y = result.pop()
        result.push(x * y)
    elif i == "/":
        x = result.pop()
        y = result.pop()
        result.push(int(x / y))
    else:
        print("Invalid instruction:",i)
        exit()
try:
    print(result.pop())
except:
    print(0)

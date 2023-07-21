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

x = input("Enter expresion : ")
Open = stack()
for char in x:
    if char in "([{":
        Open.push(char)
    if char in "}])" and len(Open) == 0:
        print(x,"close paren excess")
        exit()
    elif char in "}])":
        if char == "]":
            if Open.peek() == "[":
                Open.pop()
            else:
                print(x,"Unmatch open-close")
                exit()
        if char == ")":
            if Open.peek() == "(":
                Open.pop()
            else:
                print(x,"Unmatch open-close")
                exit()
        if char == "}":
            if Open.peek() == "{":
                Open.pop()
            else:
                print(x,"Unmatch open-close")
                exit()
if len(Open) == 0:
    print(x,"MATCH")
else:
    print(x,"open paren excess  ",len(Open),":",Open)
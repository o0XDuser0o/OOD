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

x = [action for action in input("Enter Input : ").split(",")]
tree = stack()
pstack = stack()
for action in x:
    if action[:2] == "A ":
        tree.push(int(action[2:]))
    elif action == "B":
        tree_count = 0
        tree_max = 0
        while len(tree) > 0:
            if tree.peek() > tree_max:
                tree_count += 1
                tree_max = tree.peek()
            pstack.push(tree.pop())
        print(tree_count)
        while len(pstack) > 0:
            tree.push(pstack.pop())
    elif action == "S":
        while len(tree) > 0:
            pstack.push(tree.pop())
        while len(pstack) > 0:
            if pstack.peek()%2 == 0:
                tree.push(pstack.pop() - 1)
            else:
                tree.push(pstack.pop() + 2)


class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self,item):
        self.items.append(item)

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        self.items[-1]

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        return self.items.pop()

    def __str__(self):
        return str(self.items)
    
class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
        
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0
    
    def enQueue(self,item):
        self.items.append(item)
    
    def deQueue(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items.pop(0)
    
    def front(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items[0]
    
    def last(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items[-1]
    
    def __str__(self):
        return str(self.items)
    
class sNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class dNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
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
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Can not peek empty stack")
        return self.stack[-1]
    
    def pop(self):
        if self.isEmpty():
            raise Exception("Can not pop empty stack")
        return self.stack.pop()
    
    def __str__(self):
        return str(self.stack)

class Queue:
    def __init__(self,items = None):
        if items == None:
            self.queue = []
        else:
            self.queue = items
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size() == 0
    
    def enQueue(self,item):
        return self.queue.append(item)
    
    def deQueue(self):
        if self.isEmpty():
            raise Exception("Can not dequeue empty stack")
        return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty():
            raise Exception("Can not front empty stack")
        return self.queue[0]
    
    def rear(self):
        if self.isEmpty():
            raise Exception("Can not rear empty stack")
        return self.queue[-1]
    
    def __str__(self):
        return str(self.queue)
    

    

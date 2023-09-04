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
    
code,h = input("Enter code,hint : ").split(",")
translate = Queue()
shift = ord(code[:1]) - ord(h)
for char in code:
    translate.enQueue(chr(ord(char)-shift))
print(translate)
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    
    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Dequeue from an empty queue")
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peek from an empty queue")
        return self.queue[0]
    
    def __str__(self):
        return str(self.queue)

q = Queue()
check = []
books,actions = input("Enter Input : ").split("/")
x = [action for action in actions.split(",")]
y = [book for book in books.split(" ")]
for book in y:
    q.enqueue(book)
for action in x:
    if action[:2] == "E ":
        q.enqueue(action[2:])
    elif action == "D" and not q.isEmpty():
        q.dequeue()
while not q.isEmpty():
    if q.peek() in check:
        print("Duplicate")
        exit()
    check.append(q.dequeue())
print("NO Duplicate")
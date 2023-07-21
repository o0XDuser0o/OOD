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
cash1 = Queue()
cash2 = Queue()
cash1_time = 0
cash2_time = 0
x,time = input("Enter people and time : ").split(" ")
for person in x:
    q.enqueue(person)
for i in range(1,int(time)+1):
    if cash1.isEmpty():
        cash1_time = 0
    else:
        cash1_time += 1
    if cash2.isEmpty():
        cash2_time = 0
    else:
        cash2_time += 1
    if cash1_time%3 == 0 and cash1_time > 0:
        cash1.dequeue()
    if cash2_time%2 == 0 and cash2_time > 0:
        cash2.dequeue()
    if not q.isEmpty():
        if cash1.size() < 5 :
            cash1.enqueue(q.dequeue())
        elif cash2.size() < 5:
            cash2.enqueue(q.dequeue())
    print(i,q,cash1,cash2)
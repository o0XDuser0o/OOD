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
x = [action for action in input("Enter Input : ").split(",")]
for action in x:
    if action[:2] == "E ":
        q.enqueue(action[2:])
        print("Add",action[2:],"index is",q.size() - 1)
    elif action == "D":
        try:
            txt = q.dequeue()
            print("Pop",txt,"size in queue is",q.size())
        except:
            print(-1)
if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is : ",q)
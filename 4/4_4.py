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
    
print(" ***Cafe***")
customer_list = Queue()
q = Queue()
bar1 = Queue()
bar2 = Queue()
time = 0
bar1_time = 0
bar1_out = 0
bar2_time = 0
bar2_out = 0
max_wait = 0
who = 0
num = 1
for person in input("Log : ").split("/"):
    si,pi = person.split(",")
    customer_list.enqueue([num,int(si),int(pi)])
    num+=1
while not customer_list.isEmpty() or not bar1.isEmpty() or not bar2.isEmpty():
    if not bar1.isEmpty() and bar1.peek()[2] == bar1_time:
        waiting_time = time-bar1.peek()[1]-bar1.peek()[2]
        person1 = bar1.dequeue()[0]
        if waiting_time > max_wait:
            max_wait = waiting_time
            who = person1
        bar1_time = 0
        bar1_out = 1
    if not bar2.isEmpty() and bar2.peek()[2] == bar2_time:
        waiting_time = time-bar2.peek()[1]-bar2.peek()[2]
        person2 = bar2.dequeue()[0]
        if waiting_time > max_wait:
            max_wait = waiting_time
            who = person2
        bar2_time = 0
        bar2_out = 1
    if bar1_out == 1 and bar2_out == 1:
        if person1 < person2:
            print("Time",time,"customer",person1,"get coffee")
            print("Time",time,"customer",person2,"get coffee")
        else:
            print("Time",time,"customer",person2,"get coffee")
            print("Time",time,"customer",person1,"get coffee")
        bar1_out = 0
        bar2_out = 0
    elif bar1_out == 1:
        print("Time",time,"customer",person1,"get coffee")
        bar1_out = 0
    elif bar2_out == 1:
        print("Time",time,"customer",person2,"get coffee")
        bar2_out = 0
    while not customer_list.isEmpty() and customer_list.peek()[1] == time:
        q.enqueue(customer_list.dequeue())
    while not q.isEmpty() and (bar1.isEmpty() or bar2.isEmpty()):
        print
        if bar1.isEmpty():
            bar1.enqueue(q.dequeue())
        else:
            bar2.enqueue(q.dequeue())
    if not bar1.isEmpty():
        bar1_time += 1
    if not bar2.isEmpty():
        bar2_time += 1
    time += 1

if max_wait == 0:
    print("No waiting")
else:
    print("The customer who waited the longest is :",who)
    print("The customer waited for",max_wait,"minutes")

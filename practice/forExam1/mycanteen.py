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
    
x,y = input("Enter Input : ").split("/")
canteen = []
infos = {}
for info in x.split(","):
    sec,num = info.split(" ")
    infos[num] = sec

for action in y.split(","):
    index = ""
    if action[:2] == "E ":
        if canteen == []:
            canteen.append(Queue())
            canteen[0].enQueue(action[2:])
        else:
            for i in range(len(canteen)):
                if infos[canteen[i].front()] == infos[action[2:]]:
                    index = i
            if index == "":
                canteen.append(Queue())
                canteen[-1].enQueue(action[2:])
            else:
                canteen[index].enQueue(action[2:])
    elif action == "D":
        if canteen == []:
            print("Empty")
        else:
            print(canteen[0].deQueue())
            if canteen[0].isEmpty():
                canteen.pop(0)


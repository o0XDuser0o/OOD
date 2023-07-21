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

maze = []
went = []
q = Queue()
max_x,max_y,m = input("Enter width, height, and room: ").split(" ")

# Gen map
i = 0
found_f = False
for row in m.split(","):
    column_list = []
    j = 0
    for column in row:
        column_list.append(column)
        if column == 'F':
            went.append((j,i))
            q.enqueue((j,i))
            found_f = True
        j+=1
    if len(column_list) != int(max_x):
        print("Invalid map input.")
        exit()
    maze.append(column_list)
    i+=1
if len(maze) != int(max_y):
    print("Invalid map input.")
    exit()
if not found_f:
    print("Invalid map input.")
    exit()

# Loop
scan_set = [(0,-1),(1,0),(0,1),(-1,0)]
while not q.isEmpty():
    print("Queue:",q)
    x,y = q.dequeue()
    # Scan 4 position
    for setx,sety in scan_set:
        if y+sety >= 0 and y+sety < int(max_y) and x+setx >= 0 and x+setx < int(max_x):
            pos = maze[y+sety][x+setx]
            if pos == "O":
                print("Found the exit portal.")
                exit()
            elif pos == "_" and (x+setx,y+sety) not in went:
                went.append((x+setx,y+sety))
                q.enqueue((x+setx,y+sety))
print("Cannot reach the exit portal.")
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.visited = False
        self.link = 0
    
    def mytail(self):
        i = 0
        n = self
        while n != None and not n.visited:
            n.visited = True
            n = n.next
            i += 1
        n = self
        while n != None and n.visited:
            n.visited = False
            n = n.next
        return i

inp = [[int(i) for i in act.split(">")] for act in input("Enter edges: ").split(",")]
node_map = {}
for i in inp: # scan
    if i[0] not in node_map:
        node_map[i[0]] = Node(i[0])
    if i[1] not in node_map:
        node_map[i[1]] = Node(i[1])
        node_map[i[0]].next = node_map[i[1]]
        node_map[i[1]].link += 1
    else:
        node_map[i[0]].next = node_map[i[1]]
        node_map[i[1]].link += 1

intersect = [] # intersect displayer
for v in node_map.values(): 
    if v.link > 1:
        intersect.append(v)
intersect.sort(key= lambda v : v.data)

if intersect == []:
    print("No intersection")
    exit()
for node in intersect:
    print(f"Node({node.data}, size={node.mytail()})")
print("Delete intersection then swap merge:")

for v in node_map.values(): # intersect destroyer
    if v.next != None and v.next.link > 1 :
        v.next = None
    if v.next != None and v.link > 1 :
        v.next.link -= 1
        v.next = None

n_head = [] # sorter
for k,v in node_map.items():
    if v.link == 0:
        n_head.append(node_map[k])
n_head.sort(key= lambda v : v.data)

stxt = [] # swapper
while len(n_head) != 0:
    txt = []
    size = len(n_head)
    for i in range(size):
        x = n_head.pop(0)
        txt.append(x.data)
        if x.next != None:
            n_head.append(x.next)
    for i in txt:
        stxt.append(str(i))

print(" -> ".join(stxt)) 

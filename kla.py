class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.visited = False
        self.ref_count = 0
    
    def dequeue(self):
        newhead = self.next
        return self, newhead
    
    def size(self):
        temp, count = self, 0
        while temp is not None and not temp.visited:
            temp.visited = True
            temp = temp.next
            count += 1
        temp = self
        while temp is not None and temp.visited:
            temp.visited = False
            temp = temp.next
        return count

    def __repr__(self) -> str:
        return f"Node({self.data}, size={self.size()})"




inputstr = input("Enter edges: ").split(',')
inputdata = []
for i in inputstr:
    f = int(i.split('>')[0])
    s = int(i.split('>')[1])
    inputdata.append([f, s])

dict_linkedlist = {} # dict store data: node
for eachf, eachs in inputdata:

    if eachf not in dict_linkedlist:
        dict_linkedlist.update({eachf: Node(eachf)})

    if eachs not in dict_linkedlist:
        dict_linkedlist.update({eachs: Node(eachs)})
        dict_linkedlist[eachf].next = dict_linkedlist[eachs]
        dict_linkedlist[eachs].ref_count += 1
    
    else:
        dict_linkedlist[eachf].next = dict_linkedlist[eachs]
        dict_linkedlist[eachs].ref_count += 1

intersect = []

for eachkey, eachvalue in dict_linkedlist.items():
    if eachvalue.ref_count > 1:
        intersect.append(eachvalue)
intersect.sort(key= lambda x: x.data)

if intersect == []:
    print("No intersection")
    exit()
else:
    for each in intersect:
        print(each)
print("Delete intersection then swap merge:")

for eachkey, eachvalue in dict_linkedlist.items():
    if eachvalue.next != None and eachvalue.next.ref_count > 1:
        eachvalue.next = None
    
    if eachvalue.next != None and eachvalue.ref_count > 1:
        eachvalue.next.ref_count -= 1
        eachvalue.next = None

eachhead = []
for eachkey, eachvalue in dict_linkedlist.items():
    if eachvalue.ref_count == 0:
        eachhead.append(dict_linkedlist[eachkey])
    #print(eachkey, eachvalue.data, eachvalue.next, eachvalue.ref_count)

eachhead.sort(key= lambda x: x.data)
eachheaddict = {}
for eachNode in eachhead:
    eachheaddict.update({eachNode.data: eachNode})
ans = []
# print(eachheaddict)
while eachheaddict != {}:
    for eachkey, eachvalue in eachheaddict.items():
        if eachvalue != None:
            head, newhead = eachvalue.dequeue()
            # print(head, newhead)
            ans.append(head)
            eachheaddict[eachkey] = newhead
    length = len(eachheaddict)
    l = 0
    for eachkey, eachvalue in eachheaddict.items():
        if eachvalue == None:
            l += 1
    if l == length:
        break
# print(ans)

s = ''
for each in ans:
    s += str(each.data) + ' -> '

print(s[:-4])
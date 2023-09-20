class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

customer = 0
v,res = input("Enter Input : ").split("/")
v = int(v)
res = list(map(int,res.split()))
tree = []
for i in range(v):
    tree.append(Node(0))
while res:
    for i in range(len(tree)):
        #print(i+1,tree[i].data)
        if tree[i].data == 0 and res:
            customer+=1
            day = res.pop(0)
            tree[i].data = day
            print(f'Customer {customer} Booking Van {i+1} | {day} day(s)')
            tree[i].data -= 1
        elif tree[i].data > 0:
            tree[i].data -= 1
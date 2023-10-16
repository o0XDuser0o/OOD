class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def hash(key):
        return sum(ord(x) for x in key)

    def __repr__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size, maxcollision):
        self.size = size
        self.maxcol = maxcollision
        self.hashTable = [None] * size
    
    def insert(self, data):
        index = Data.hash(data.key) % self.size
        n = 1
        col = 1
        
        while self.hashTable[index] is not None:
            if self.isFull():
                return True
            if col > self.maxcol:
                print("Max of collisionChain")
                return True
            print(f"collision number {col} at {index}")
            index = (Data.hash(data.key) + n*n) % self.size
            col += 1
            n += 1

        if self.hashTable[index] is None:
            self.hashTable[index] = data
            return

    def isFull(self):
        if None in self.hashTable:
            return False
        else:
            return True
            

    def printHash(self):
        index = 1
        for i in self.hashTable:
            print(f"#{index}	{i}")
            index += 1
        print('---------------------------')

print(" ***** Fun with hashing *****")
inp = input("Enter Input : ").split('/')
tablesize = int(inp[0].split()[0])
maxcol = int(inp[0].split()[1])
data = inp[1].split(',')
hash = Hash(tablesize, maxcol)
for i in data:
    key = i.split()[0]
    value = i.split()[1]
    d = Data(key, value)
    if hash.isFull():
        print('This table is full !!!!!!')
        exit()
    hash.insert(d)
    hash.printHash()
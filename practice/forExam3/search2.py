class Hash:
    def __init__(self, size, maxcollision, threshold):
        self.size = size
        self.maxcol = maxcollision
        self.hashTable = [None] * size
        self.threshold = threshold
    
    def insert(self, data):
        index = data % self.size
        n = 1
        col = 1

        while self.hashTable[index] is not None:
            
            print(f"collision number {col} at {index}")
            index = (data + (n * n)) % self.size

            if col >= self.maxcol:
                print("****** Max collision - Rehash !!! ******")
                self.rehashing()
                index = data % self.size
            
            col += 1
            n += 1

        if self.hashTable[index] is None:
            #self.hashTable[index] = data
            if (((self.findTotalElements() + 1) / self.size) * 100) >= self.threshold:
                print("****** Data over threshold - Rehash !!! ******")
                self.rehashing()
                self.insert(data)
            else:
                self.hashTable[index] = data
            
    
    def rehashing(self):
        olddata = []
        for i in self.hashTable:
            if i != None:
                olddata.append(i)

        newSize = self.findPrimeNumber(self.size)
        self.size = newSize
        self.hashTable = [None] * newSize
       
        for i in olddata[::-1]:
            self.insert(i)

    def findTotalElements(self):
        n = 0
        for i in self.hashTable:
            if i is not None:
                n += 1
        return n
    
    def findPrimeNumber(self, num):
        num *= 2
        flag = True
        while flag: 
            for i in range(2,num):
                if num % i == 0:
                    num += 1
                    break
            else:
                return num

    def findThreshold(self):
        elementNum = self.findTotalElements()
        return elementNum / self.size


    def printHash(self):
        index = 1
        for i in self.hashTable:
            print(f"#{index}	{i}")
            index += 1
        print('----------------------------------------')


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split('/')
tablesize = int(inp[0].split()[0])
maxcol = int(inp[0].split()[1])
threshold = int(inp[0].split()[2])
data = inp[1].split()
hash = Hash(tablesize, maxcol, threshold)
print("Initial Table :")
hash.printHash()
for i in data:
    print('Add : ' + str(i))
    hash.insert(int(i))
    hash.printHash()
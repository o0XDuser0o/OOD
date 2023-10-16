class Stack:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

    def push(self,item):
        self.items.append(item)

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        self.items[-1]

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        return self.items.pop()

    def __str__(self):
        return str(self.items)
    
class Queue:
    def __init__(self,items = None):
        if items == None:
            self.items = []
        else:
            self.items = items
        
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0
    
    def enQueue(self,item):
        self.items.append(item)
    
    def deQueue(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items.pop(0)
    
    def front(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items[0]
    
    def last(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        return self.items[-1]
    
    def __str__(self):
        return str(self.items)
    
class sNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class dNode:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
def quickSort(lst,l,r):
    if l+1 == r:
        if lst[l] > lst[r]:
            lst[l],lst[r] = lst[r],lst[l]
        return
    if l < r:
        pivot = lst[l]
        i,j = l+1,r
        while i<j:
            while i<r and lst[i] <= pivot:
                i+=1
            while j>l and lst[j] >= pivot:
                j-=1
            #print(i,j)
            if i<j:
                lst[i],lst[j] = lst[j],lst[i]
        if j != l:
            lst[l],lst[j] = lst[j],pivot
        quickSort(lst,l,j-1)
        quickSort(lst,j+1,r)

def mergeSort(lst:list,l,r):
    if l<r:
        c = (l+r)//2
        lst = mergeSort(lst,l,c)
        lst = mergeSort(lst,c+1,r)
        lst = merge(lst,l,c+1,r)
    return lst

def merge(lst,l,r,re):
    result = []
    start = l
    le = r-1
    while l<=le and r<=re:
        if lst[l] < lst[r]:
            result.append(lst[l])
            l += 1
        else:
            result.append(lst[r])
            r += 1
    while l<=le:
        result.append(lst[l])
        l += 1
    while r<=re:
        result.append(lst[r])
        r += 1
    for r in result:
        lst[start] = r
        start += 1
        if start > re:
            break
    return lst

lst = [5,8,4,6,8,2,3,4,7]
#quickSort(lst,0,len(lst)-1)
lst = mergeSort(lst,0,len(lst)-1)
print(lst)
    
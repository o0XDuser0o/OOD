def insertMinHeap(h:list,i):
    insertdata = h[i]
    upIndex = (i-1)//2
    while i>0 and insertdata < h[upIndex]:
        h[i] = h[upIndex]
        i = upIndex
        upIndex = (i-1)//2
    h[i] = insertdata
    return h

def deleteMinHeap(h:list,last):
    pass

lst = []
isl = [68,65,32,24,26,21,19,13,16,14]

for i in range(len(isl)):
    lst.append(isl[i])
    lst = insertMinHeap(lst,i)
    print(lst)
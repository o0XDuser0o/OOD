def bubbleSort(data:list):
    for i in range(len(data)-1,0,-1):
        swap = False
        for j in range(0,i):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                swap = True
        if not swap:
            break
    return data

def selectSort(data:list):
    for i in range(len(data)-1,0,-1):
        biggest = data[0]
        big_i = 0
        for j in range(1,i+1):
            if data[j] > biggest:
                biggest = data[j]
                big_i = j
        data[big_i],data[i] = data[i],data[big_i]
    return data

def insertSort(data:list):
    for i in range(1,len(data)):
        ptr = data[i]
        for j in range(i,-1,-1):
            if j>0 and ptr <= data[j-1]:
                data[j] = data[j-1]
            else:
                data[j] = ptr
                break
    return data

def shellSort(data:list,gl):
    for g in gl:
        for i in range(g,len(data)):
            ptr = data[i]
            for j in range(i,-1,-g):
                if j >= g and ptr < data[j-g]:
                    data[j] = data[j-g]
                else:
                    data[j] = ptr
                    break
    return data

def heapSort(data):
    for i in range(len(data)):
        data = heapInsert(data,i)
    for i in range(len(data)-1,-1,-1):
        data = heapDelete(data,i)
    return data
    

def heapInsert(lst,i):
    ptr_data = lst[i]
    prev_i = (i-1)//2
    while i>0 and lst[prev_i] > ptr_data:
        lst[i] = lst[prev_i]
        i = prev_i
        prev_i = (prev_i-1)//2
    lst[i] = ptr_data
    return lst

def heapDelete(lst,i):
    ptr_data = lst[i]
    lst[i] = lst[0]
    ci = 0
    lni = ci*2+1
    found = False
    while lni < i and not found:
        rni = lni
        if lni+1 < i:
            rni += 1
        si = lni
        if lst[lni] > lst[rni]:
            si = rni
        if lst[si] < ptr_data:
            lst[ci] = lst[si]
            ci = si
            lni = ci*2+1
        else:
            found = True
    lst[ci] = ptr_data
    return lst

def mergeSort(data,l,r):
    if l < r:
        m = (l+r)//2
        data = mergeSort(data,l,m)
        data = mergeSort(data,m+1,r)
        data = merge(data,l,m,m+1,r)
    return data

def merge(data,sl,el,sr,er):
    result = []
    start = sl
    while sl <= el and sr <= er:
        if data[sl] < data[sr]:
            result.append(data[sl])
            sl += 1
        else:
            result.append(data[sr])
            sr += 1
    while sl <= el:
        result.append(data[sl])
        sl += 1
    while sr <= er:
        result.append(data[sr])
        sr += 1
    for r in result:
        lst[start] = r
        start += 1
        if start > er:
            break
    return lst

def quickSort(data,l,r):
    if l+1 == r:
        if data[l] > data[r]:
            data[l],data[r] = data[r],data[l]
        return data
    if l < r:
        pivot = data[l]
        i,j = l+1,r
        while i<j:
            while i<r and data[i] <= pivot:
                i+=1
            while j>l and data[j] >= pivot:
                j-=1
            if i<j:
                data[i],data[j] = data[j],data[i]
        if j != l:
            data[l],data[j] = data[j],pivot
        print(data)
        data = quickSort(data,l,j-1)       
        data = quickSort(data,j+1,r)
    return data        




lst = [2,4,6,8,3,7,0,1,56,17,9]
print(bubbleSort(lst))
lst = [2,4,6,8,3,7,0,1,56,17,9]
print(selectSort(lst))
lst = [2,4,6,8,3,7,0,1,56,17,9]
print(insertSort(lst))
lst = [2,4,6,8,3,7,0,1,56,17,9]
gl = [5,3,1]
print(shellSort(lst,gl))
lst = [2,4,6,8,3,7,0,1,56,17,9]
print(heapSort(lst))
lst = [2,4,6,8,3,7,0,1,56,17,9]
print(mergeSort(lst,0,len(lst)-1))
lst = [2,4,6,8,3,7,0,1,56,17,9]
print(quickSort(lst,0,len(lst)-1))
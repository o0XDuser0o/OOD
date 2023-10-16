def insertionSort(data):
    for i in range(1,len(data)):
        if data[i] < 0:
            continue
        ptr = data[i]
        index = i
        for j in range(i,-1,-1):
            if data[j-1] < 0:
                continue
            elif ptr < data[j-1] and j > 0:
                data[index],data[j-1] = data[j-1],data[index]
                index = j-1
        #print(data)
    return data

        

inp = list(map(int,input("Enter Input : ").split()))
print(" ".join(list(map(str,insertionSort(inp)))))
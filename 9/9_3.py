def insertionSort(s:list,us:list):
    if us:
        num = us.pop(0)
        s,index = _insertS(s,num,0)
        if us:
            print(f'insert {num} at index {index} : {s} {us}')
        else:
            print(f'insert {num} at index {index} : {s}')
        return insertionSort(s,us)
    return s

def _insertS(s:list,num:int,index:int):
    if len(s) <= index:
        s.append(num)
        return s,index
    if s[index] > num:
        s.insert(index,num)
        return s,index
    s,index = _insertS(s,num,index + 1)
    return s,index 

inp = list(map(int,input("Enter Input : ").split()))
x = inp.pop(0)
inp = insertionSort([x],inp)
print("sorted")
print(inp)
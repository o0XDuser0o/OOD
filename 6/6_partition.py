#จงยำเกรงพี่ซันฟง

def partition(left,num,s,path):
    global i
    numOfPath = 0
    if num > 0:
        if left - num == 0:
            path.append(num)
            if s > i:
                print(' '.join(map(str, path)))
            elif s == i:
                print("...")
            path.pop(-1)
            i += 1
            numOfPath += 1
        elif left - num > 0 and left - num >= num:
            path.append(num)
            numOfPath += partition(left - num,num,s,path)
            path.pop(-1)
        elif left - num > 0:
            path.append(num)
            numOfPath += partition(left - num,num-1,s,path)
            path.pop(-1)
        return numOfPath + partition(left,num-1,s,path)
    return numOfPath

i = 0
n, s = map(int ,input('Enter n, s: ').split())
print(partition(n,n,s,[]))

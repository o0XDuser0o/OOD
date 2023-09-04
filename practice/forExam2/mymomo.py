def groupup(data,x,k,dump):
    #print(data,k,dump,x)
    if k == 1 and data != []:
        return False
    if data == [] and k >= 1:
        return True
    if sum(dump) + data[:1][0] > x:
        dump = []
        k -= 1
    dump.append(data[:1][0])
    return groupup(data[1:],x,k,dump)
    

def rightx(data,x,k):
    if groupup(data,x,k,[]):
        return x
    return rightx(data,x+1,k)

l,k = input("input l/k: ").split("/")
k = int(k)
data = l.split(" ")
data = list(map(int,data))
maxn = max(data)
print(rightx(data,maxn,k))

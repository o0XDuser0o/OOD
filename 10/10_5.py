def theFunc(data,k):
    def grouppUp(mw):
        sumw = 0
        b = 0
        for i in data:
            #print(i,sumw,b)
            if sumw + i > mw:
                b += 1
                sumw = i
            else:
                sumw+=i
        if sumw != 0:
            b+=1
        if b == k:
            return True
        else:
            return False        

    x = max(data)
    while not grouppUp(x):
        x+=1
    return x

l,k = input("Enter Input : ").split("/")
k = int(k)
data = l.split(" ")
data = list(map(int,data))
print("Minimum weigth for",k,"box(es) =",theFunc(data,k))

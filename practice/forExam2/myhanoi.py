def printpole(maxpole):
    global a,b,c
    if maxpole == 0:
        print(f'{a[0]} {b[0]} {c[0]}')
        return
    ca = "|"
    cb = "|"
    cc = "|"
    if len(a[1]) >= maxpole:
        ca = a[1][maxpole-1]
    if len(b[1]) >= maxpole:
        cb = b[1][maxpole-1]
    if len(c[1]) >= maxpole:
        cc = c[1][maxpole-1]
    print(f'{ca} {cb} {cc}')
    printpole(maxpole-1)
    return

def move(ori,des,maxpole):
    print(f'{ori[0]} to {des[0]}')
    des[1].append(ori[1].pop())
    printpole(maxpole)
    return ori,des

def hanoi(n,ori,des,pole,maxp): #ori = origin des = destinstion pole = เสาที่ไม่ใช้
    if n == 1:
        ori,des = move(ori,des,maxp)
        return ori,des,pole
    ori,pole,des = hanoi(n-1,ori,pole,des,maxp)
    ori,des = move(ori,des,maxp)
    pole,des,ori = hanoi(n-1,pole,des,ori,maxp)
    return ori,des,pole

num = int(input("input: "))
a = ["A",list(range(num,0,-1))]
b = ["B",[]]
c = ["C",[]]
hanoi(num,a,c,b,num)
def loopinput(mylist,w):
    if w == 0:
        return mylist
    mylist.append(input().split(" "))
    loopinput(mylist,w-1)
    return mylist

def deleteisland(mylist,y,x):
    if y < 0 or y >= len(mylist) or x < 0 or x >= len(mylist[0]) or mylist[y][x] == ".":
        return mylist
    mylist[y][x] = "."
    mylist= deleteisland(mylist,y-1,x)
    mylist= deleteisland(mylist,y,x+1)
    mylist= deleteisland(mylist,y+1,x)
    mylist= deleteisland(mylist,y,x-1)
    return mylist
    

h,w = map(int,input("Enter input: ").split(" "))
mymap = loopinput([],w)
count = 0

for i in range(w):
    for j in range(h):
        if mymap[i][j] == "#":
            count += 1
            mymap = deleteisland(mymap,i,j)

print(count)



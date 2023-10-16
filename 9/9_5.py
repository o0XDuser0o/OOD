def mysort(lst:list):
    lst = mergeSort(teams,0,len(teams)-1)
    return lst

def mergeSort(lst:list,l,r):
    if l<r:
        c = (l+r)//2
        lst = mergeSort(lst,l,c)
        lst = mergeSort(lst,c+1,r)
        lst = merge(lst,l,c+1,r)
    return lst

def merge(lst:list,l,r,re):
    result = []
    start = l
    le = r-1
    while l<=le and r<=re:
        if lst[l][1] > lst[r][1]:
            result.append(lst[l])
            l += 1
        elif lst[l][1] == lst[r][1] and lst[l][2] > lst[r][2]:
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

teams = []
for t in input("Enter Input : ").split("/"):
    name,w,l,d,s,c = t.split(",")
    point = int(w)*3+int(d)
    gd = int(s)-int(c)
    teams.append([name,point,gd])

teams = mysort(teams)
print("== results ==")
for team in teams:
    print("['"+team[0]+"', {'points': "+str(team[1])+"}, {'gd': "+str(team[2])+"}]")


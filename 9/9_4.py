def quickSort(lst,l,r):
    if l+1 == r:
        if lst[l] > lst[r]:
            lst[l],lst[r] = lst[r],lst[l]
        return lst
    if l < r:
        pivot = lst[l]
        i,j = l+1,r
        while i<j:
            while i<r and lst[i] <= pivot:
                i+=1
            while j>l and lst[j] >= pivot:
                j-=1
            if i<j:
                lst[i],lst[j] = lst[j],lst[i]
        if j != l:
            lst[l],lst[j] = lst[j],pivot
        lst = quickSort(lst,l,j-1)
        lst = quickSort(lst,j+1,r)
    return lst


alpha_dict = {}
alpha_list = []
for char in input("Enter Input : ").split():
    v = 0
    for c in char:
        if c.isalpha():
            v = ord(c)
            break
    alpha_list.append(v)
    alpha_dict[v] = char

alpha_list = quickSort(alpha_list,0,len(alpha_list)-1)
for v in alpha_list:
    print(alpha_dict[v],end=" ")




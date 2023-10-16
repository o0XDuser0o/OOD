def bi_search(l, r, arr, x):
    if r < l:
        return False
    m = (l+r)//2
    if arr[m] < x:
        return bi_search(m+1,r,arr,x)
    elif arr[m] > x:
        return bi_search(l,m-1,arr,x)
    else:
        return True


inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))
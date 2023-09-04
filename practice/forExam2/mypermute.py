def txtinlist(data,path):
    if path != []:
        return str(data[path[0]]) + txtinlist(data,path[1:])
    return ""

def permute(data,k,n,path):
    global ans
    if k == 0:
        if txtinlist(data,path) not in ans:
            return ans.append(txtinlist(data,path))
        return
    if n <= len(data) - 1:
        if n not in path:
            path.append(n)
            permute(data,k-1,0,path)
            path.pop()
        permute(data,k,n+1,path)
    return

s, k = input("Enter a string and k: ").split('/')
ans = []
k = int(k)
s = list(s)
if k < 0:
    print("Invalid value of k. k must be a non-negative integer.")
elif k > len(s):
    print('Invalid value of k. k must be less than or equal to the length of the string.')
else:
    permute(s,k,0,[])
    print(ans)
def pantip(k, n, arr, path):
    numOfPattern = 0
    if arr:
        if k - arr[n] == 0:
            path.append(arr[n])
            print(' '.join(map(str, path)))
            path.pop(-1)
            numOfPattern += 1
        elif k - arr[n] > 0:
            path.append(arr[n])
            numOfPattern += pantip(k - arr[n], n, arr[1:], path)
            path.pop(-1)
        return pantip(k, n, arr[1:], path) + numOfPattern
    return numOfPattern

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))
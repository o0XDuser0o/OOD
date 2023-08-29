#code by korphai

def move(n,fromt,waitt,tot,maxn):
    if n == 1:
        tot[0].append(fromt[0].pop())
        print(f'move {n} from  {fromt[1]} to {tot[1]}')
        printHanoi(maxn)
        return
    move(n-1,fromt,tot,waitt,maxn)
    trans = fromt[0].pop()
    tot[0].append(trans)
    print(f'move {n} from  {fromt[1]} to {tot[1]}')
    printHanoi(maxn)
    move(n-1,waitt,fromt,tot,maxn)

def beginning_harnoid(n, char):
    if n <= 0:
        return [char]
    else:
        return [list(range(n, 0, -1)), char]

def printHanoi(n):
    global a, b, c
    if n < 0:
        return

    if len(a[0]) <= n:
        print('|  ', end='')
    else:
        print(f'{a[0][n]}  ', end='')

    if len(b[0]) <= n:
        print('|  ', end='')
    else:
        print(f'{b[0][n]}  ', end='')

    if len(c[0]) <= n:
        print('|')
    else:
        print(f'{c[0][n]}')

    return printHanoi(n-1)
        
n = int(input("Enter Input : "))
a = beginning_harnoid(n, 'A')
b = [[],'B']
c = [[],'C']
printHanoi(n)
move(n,a,b,c,n)
def dectobin(n):
    if n <= 1:
        return str(n)
    return dectobin(n//2) + str(n%2)

def printbit(n,digit):
    if n <= 0:
        print(dectobin(n).rjust(digit,"0"))
        return
    printbit(n-1,digit)
    print(dectobin(n).rjust(digit,"0"))

digit = int(input("input: "))
n = 2**digit - 1
printbit(n,digit)
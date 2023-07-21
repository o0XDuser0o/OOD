print(" *** Divisible number ***")
x = int(input("Enter a positive number : "))
result = []
if x == 0:
    print("0 is OUT of range !!!")
else:
    for i in range(1,x+1):
        if x % i == 0:
            result.append(i)
    print("Output ==>",' '.join(map(str, result)))
    print("Total ==>",len(result))
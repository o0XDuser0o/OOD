def Range(num):
    result = ""
    if len(num) == 1:
        i = 0
        while(i < num[0]):
            result = result + str(i) +".0, "
            i+=1
    elif len(num) == 2:
        i = num[0]
        while(i < num[1]):
            result = result + str(round(i,3)) +", "
            i+=1
    else:
        i = num[0]
        while(i < num[1]):
            result = result + str(round(i,3)) +", "
            i+=num[2]

    return "("+result[:-2]+")"

print("*** New Range ***")
r = [float(num) for num in input("Enter Input : ").split(" ")]
print(Range(r))
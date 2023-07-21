print("*** String Rotation ***")
x,y = input("Enter 2 strings : ").split(" ")
resultx = list(x)
resulty = list(y)
resultx = resultx[-2:]+resultx[:-2]
resulty = resulty[3:]+resulty[:3]
i = 1
while not x == ''.join(resultx) or not y == ''.join(resulty):
    if i <= 5:
        print(i,''.join(resultx),''.join(resulty))
    elif i == 6:
        print(" . . . . .")
    resultx = resultx[-2:]+resultx[:-2]
    resulty = resulty[3:]+resulty[:3]
    i += 1
print(i,''.join(resultx),''.join(resulty))
print("Total of ",i,"rounds.")
print(" *** String count ***")
x = input("Enter message : ")
uc_count = 0
lc_count = 0
uc = []
lc = []

for char in x:
    if char.islower():
        lc_count += 1
        if char not in lc:
            lc.append(char)
    elif char.isupper():
        uc_count +=1
        if char not in uc:
            uc.append(char)

uc.sort()
lc.sort()

print("No. of Upper case characters :",uc_count)
print("Unique Upper case characters : ",end="")
[print(i, end='  ') for i in uc]
print("\nNo. of Lower case Characters :",lc_count)
print("Unique Lower case characters : ",end="")
[print(i, end='  ') for i in lc]
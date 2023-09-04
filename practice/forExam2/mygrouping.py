def bc(txt,char):
    if txt[-1:] != char or txt == "":
        return 0
    return 1 + bc(txt[:-1],char)

def fc(txt,char):
    if txt[:1] != char or txt == "":
        return 0
    return 1 + fc(txt[1:],char)

txt,i = input("input number : ").split(",")
i = int(i)
if txt == "":
    print("Output : List is entry")
elif i > len(txt):
    print("Output : Pin number out of range")
elif i < 1:
    print("Output : Pin number less than 1")
else:
    print(f'char = {txt[i-1]}')
    count = 1 + bc(txt[:i-1],txt[i-1]) + fc(txt[i:],txt[i-1])
    print(count)
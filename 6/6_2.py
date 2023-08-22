def parindome(txt):
    if txt == "":
        return "palindrome"
    elif txt[:1] == txt[-1:]:
        return parindome(txt[1:-1])
    else:
        return "not palindrome"
txt = input("Enter Input : ")
print(f"'{txt}'","is",parindome(txt))


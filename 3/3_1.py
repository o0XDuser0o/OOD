x = input("Enter Input : ")
l = [char for char in x]
if x.count("[") != x.count("]") or x.count('(') != x.count(")"):
    print("Parentheses : Unmatched ! ! !")
else:
    print("Parentheses : Matched ! ! !")
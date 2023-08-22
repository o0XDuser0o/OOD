def gcd(x,y):
    if y == 0:
        if x<0:
            return x*-1
        return x
    return gcd(y,x%y)

x,y = input("Enter Input : ").split(" ")
x = int(x)
y = int(y)
if x == 0 and y == 0:
    print("Error! must be not all zero.")
elif x >= y:
    print(f"The gcd of {x} and {y} is : {gcd(x,y)}")
else:
    print(f"The gcd of {y} and {x} is : {gcd(y,x)}")
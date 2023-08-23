# x = "12345"
# y = x[-2:]
# z = x[:-2]
# print(x,y,z)

# x = float(input())
# print(type(x),x)

# x, nsr= input("Enter number and shiftcount : ").split()
# int(x)
# int(nsr)
# print(int(x) >> int(nsr))

# num = int(input())
# a = input()
# b = input()
# print(((a+b)*num)[:num])

# def move(n,A,C,B):
#     if n == 1:
#         print(n,"from",A,"to",C)
#     else:
#         move(n-1,A,B,C)
#         print(n,"from",A,"to",C)
#         move(n-1,B,C,A)

# move(5,'A','B','C')
num = 5
print(str(bin(2)[2:]).rjust(num,"0"))
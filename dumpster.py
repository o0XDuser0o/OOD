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

# num = 5
# print(str(bin(2)[2:]).rjust(num,"0"))
# lst = list(map(int,input().split()))
# print(sum(lst))
def verify_pw(pw):
    # YOUR CODE HERE
    password = str(pw)
    Big_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    number = '0123456789'
    specailcharacter = ' @ $'
    lst = []

    if len(password) < 8 :
        lst.append(1)
    for i in password:
        if i in Big_alphabet:
            break
    else:
        lst.append(2)
    for i in password:
        if i in small_alphabet:
            break
    else:
        lst.append(3)
    for i in password:
        if i in number:
            break
    else:
        lst.append(4)
    for i in password:
        if i in specailcharacter:
            lst.append(0)
            break
    else:
        lst.append(5)

    return lst
print(verify_pw(1234))
result = verify_pw("ireur32")
print(len(verify_pw("ireur32")))
print(result)


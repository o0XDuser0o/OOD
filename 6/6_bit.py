def dec_to_bin(n):
    txt = ''
    if n > 1:
        txt += dec_to_bin(n//2)
    return txt + str(n % 2)

def run_binary(max_num):
    if max_num == 0:
        print(str(bin(max_num)[2:]).rjust(digit,'0'))
        return
    else:
        run_binary(max_num-1)
        print(str(bin(max_num)[2:]).rjust(digit,'0'))
        return
digit = int(input("Enter Number : "))
if digit < 0:
    print("Only Positive & Zero Number ! ! !")
    exit()
run_binary(pow(2,digit)-1)

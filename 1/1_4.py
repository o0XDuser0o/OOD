def odd_list(al):
    # เติมส่วนของคำสั่ง
    odd_num_list = []
    for number in al:
        if number%2 != 0:
            odd_num_list.append(number)
    return odd_num_list

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)
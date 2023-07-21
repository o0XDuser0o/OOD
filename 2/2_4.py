num_list = [int(num) for num in input("Enter Your List : ").split(" ")]
result = []
if len(num_list) > 2:
    for i in range(len(num_list)):
        for j in range(i+1,len(num_list)):
            for k in range(j+1,len(num_list)):
                if num_list[i] + num_list[j] + num_list[k] == 5:
                    x = [num_list[i],num_list[j],num_list[k]]
                    x.sort()
                    if x not in result:
                        result.append(x)
    print(result)
else:
    print("Array Input Length Must More Than 2")

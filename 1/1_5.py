print("*** Fun with countdown ***")
num_list = [int(num) for num in input("Enter List : ").split(" ")]
num_list.reverse()
result = []
for i in range(len(num_list)):
    if num_list[i] == 1:
        count_list = []
        j = i
        while j+1 < len(num_list) and num_list[j] == num_list[j+1] - 1:
            count_list.append(num_list[j])
            j+=1
        count_list.append(num_list[j])
        count_list.reverse()
        result.append(count_list)
result.reverse()
print([len(result), result])




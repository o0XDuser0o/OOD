inp = list(map(int,input("Data : ").split()))
result = []
i = 0
maxl = 0
for num in inp:
    if result and result[-1] > num:
        result.pop()
        while result and result[-1] > num:
            result.pop()
    if not result or result[-1] < num:
        result.append(num)
    if len(result) > maxl:
        maxl = len(result)
    i += 1
    print(f'{i} : {result}')
print(f'longest increasing subsequence : {maxl}')
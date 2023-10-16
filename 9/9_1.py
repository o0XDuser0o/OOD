def bubbleSort(data):
    lastswaped = None
    for i in range(len(data)-1,0,-1):
        swaped = False
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                lastswaped = data[j+1]
                swaped = True
        if swaped and i != 1:
            print(f'{len(data)-i} step : {data} move[{lastswaped}]')
            lastswaped = None
        else:
            print(f'last step : {data} move[{lastswaped}]')
            break
    return data

inp = list(map(int,input("Enter Input : ").split()))
bubbleSort(inp)

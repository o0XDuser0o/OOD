def staircase(n,start):
    if start == n:
        return "Not Draw!"
    if n > 0:
        if n - start == 1:
            return (n-start-1)*"_" + (start+1) *"#" +"\n"
        else:
            return (n-start-1)*"_" + (start+1) *"#" +"\n" + staircase(n,start+1)
    else:
        if n - start == -1:
            return (start*-1)*"_" + ((n-start)*-1) *"#" +"\n"
        else:
            return (start*-1)*"_" + ((n-start)*-1) *"#" +"\n" + staircase(n,start-1)

print(staircase(int(input("Enter Input : ")),0))
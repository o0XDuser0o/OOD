print("*** TorKham HanSaa ***")
game = [word for word in input("Enter Input : ").split(",")]
history = []
counter = 0

for word in game:
    if word[:1] == "X" and len(word) < 2:
        break
    elif word[:1] == "R" and len(word) < 2:
        print("game restarted")
        history = []
        counter = 0
    elif word[:2] == "P " and len(word) > 3:
        w = word[2:]
        if history == []:
            history.append(w)
            print("'"+w+"' -> "+str(history))
            counter += 1
        else:
            if w[:2].upper() == history[counter-1][-2:].upper() and w not in history:
                history.append(w)
                print("'"+w+"' -> "+str(history))
                counter += 1
            else:
                print("'"+w+"' -> game over")
    else:
        print("'"+word +"' is Invalid Input !!!")
        break

print("*** Election ***")
count_vote = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
num = int(input("Enter a number of voter(s) : "))
vote_list = [int(vote) for vote in input().split(" ")]
for vote in vote_list:
    if vote < 21 and vote > 0:
        count_vote[vote-1] += 1
max_vote = max(count_vote)
if max_vote == 0:
    print("*** No Candidate Wins ***")
else:
    for i in range(20):
        if count_vote[i] == max_vote:
            print(i+1,end=" ")

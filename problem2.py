import random

print("You are playing game")
score = random.randint(1,60)

with open("Hi-score.txt") as f:
    hiscore=f.read()
    if(hiscore)!="":
        hiscore=int(hiscore)
    else:
        hiscore=0
        
print(f"Your score : {score}")
if(score>hiscore):
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
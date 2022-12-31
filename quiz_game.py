print("Welcome to Quiz !")

playing=input("Do You want to play ?")

if playing.lower()!="yes":
    quit()
print("Okay ! Let's Play :)")
score=0

answer=input("What does CPU stand for?")
if answer.lower()=="central processing unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("What does SSD stand for?")
if answer.lower()=="solid state drives":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("What does HDD stand for?")
if answer.lower()=="hard disk drives":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("What does RAM stand for?")
if answer.lower()=="random access memory":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("Which year has 366 days?")
if answer.lower()=="leap year":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
answer=input("What does GPU stand for?")
if answer.lower()=="graphics processing unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
print("You got "+str(score)+"questions correct!")
print("You got "+str((score/5)*100)+"%.")
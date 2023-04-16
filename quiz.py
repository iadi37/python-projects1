print("Welcome to the quiz!!")

playing =input("Do you want to play? ")
if playing.lower() !="yes":
    quit()
print("Okay! Let's Play:)")
score=0

answer = input("What does RAM stand for? ")

if answer.lower()=="random access memory":
    print("Correct!🥳")
    score+=1
else:
    print("Incorrect😥")

answer = input("What does CPU  stand for? ")

if answer.lower()=="central processing unit":
    print("Correct!🥳")
    score+=1
else:
    print("Incorrect😥")

answer = input("What does API stand for? ")

if answer.lower()=="application programming interface":
    print("Correct!🥳")
    score+=1
else:
    print("Incorrect😥")

answer = input("What does GPU  stand for? ")

if answer.lower()=="graphics processing unit":
    print("Correct!🥳")
    score+=1
else:
    print("Incorrect😥")

answer = input("What does CN stand for? ")

if answer.lower()=="computer network":
    print("Correct!🥳")
    score+=1
else:
    print("Incorrect😥")

answer = input("What does OS stand for? ")

if answer.lower()=="operating system":
    print("Correct!🥳")
    score+=1
else:
    print("Incorrect😥")

print("You got " + str(score) + " question correct 😎😎😎")
print("You got " +str((score/6)*100)+ " %. 🙌🙌🙌 ")




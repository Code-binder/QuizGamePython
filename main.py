print("Welcome to my computer quiz")

playing = input("Do you want to play? ")



if playing != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does a CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does a GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1

else:
    print("Incorrect!")
    

answer = input("What does a RAM stand for? ")
if answer.lower() =="random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does a PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " quesions correct")
print("You got " + str((score / 4 * 100)) + " %")
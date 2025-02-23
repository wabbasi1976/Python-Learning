print("Welcome to my computer quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Lets play:) ")
    score = 0
answer = input("WHat does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("incorrect!")
answer = input('PS stands for? ')
if answer.lower() == "power supply":
    print('correct!')
    score += 1
else: 
    print('incorrect!')
answer = input('ram stands for? ')
if answer.lower() == "randam access memory":
    print('correct!')
    score += 1
else: 
    print('incorrect!')
    
answer = input('rom stands for? ')
if answer.lower() == "read only memory":
    print('correct!')
    score += 1
else: 
    print('incorrect!')
print("Total Score = ", score)
print("You got " + str(score) + " Questions correct")
print("You got " + str(score /4 *100) + " % Correct")


print("Welcome to my quiz game !")

playing = input("Do you want to play this game ? ")

if playing.lower() != "yes":
    quit()

print(" Lets play! ")    
score = 0


answer = input("What does CD stand for? ")
if answer.lower() == "compact disk":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")    

answer = input("What does TMI stand for? ")
if answer.lower() == "too much information ":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")        

answer = input("what does lol stand for? ")
if answer.lower() == "laughing out loud":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")    

answer = input("What does nvm stand for? ")
if answer.lower() == "nevermind":
    print("Correct! ")
    score += 1
else:
    print("Incorrect! ")    

print("You got " + str(score) + " questions correct! ")
print("You got " + str((score/4) * 100) + "%. ")
# Level One
# In level one, the computer generates a random number between 1 and 10 
# and the user has 3 guesses to pick the correct number. The computer will tell you 
# if you are too high or too low.

import random

isWinner = False
cpuNum = random.randint(1, 10)
print(cpuNum)

count = 3
while count > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    count -= 1
    print("You have",count,"guesses remaining")
    if guess > cpuNum:
        print("Too high")
    elif guess < cpuNum:
        print("Too low")
    else:
        print("You win! ")
        isWinner = True
        break

if isWinner == False:
    print("You lose :^( The correct number was", cpuNum)
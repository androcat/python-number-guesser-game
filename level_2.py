# Level Two
# In level two, the game is reversed and the user picks a number between 1 and 10. 
# The computer then has 3 guesses to select the correct answer. The user will tell the 
# computer if they are correct or incorrect.

import random

isWinner = False
count = 3

num = int(input("Hello, I am CPU. I have 3 tries to guess your number. Enter a number between 1 and 10: "))

while count > 0:
    cpu = random.randint(1, 10)
    count -= 1
    print("My guess is",cpu)
    user = input("Am I correct? (y/n): ")
    if user == "n":
        print("Aww :^( Alright, let me try again.")
    else:
        print("Yay I guessed your number! :^D")
        isWinner = True
        break
        
if isWinner == False:
    print("Aww looks like I ran out of guesses. Guess there's always next time. Bye bye !")
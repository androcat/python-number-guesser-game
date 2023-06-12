# Level Four
# In level four, give the user an option to play against the computer or to think of a number 
# for the computer to guess.

import random

player = input("Welcome to The Guessing Game ! Would you like (a) guess my number or (b) make me guess? (a/b): ")

if player == "a":
    isWinner = False
    cpuNum = random.randint(1, 10)

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
elif player == "b":
    player = input("Now, would you like me to (1) try to guess in 3 tries or (2) see how long it takes me to guess your number? (1/2)")
    if player == "1":
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
    elif player == "2":
        count = 0

        num = int(input("Hello, I am CPU. Tell me if I my guess is too high or too low until I get your number. Enter a number between 1 and 10 for me to guess: "))
        cpu = 5

        min = 1
        max = 11

        print("My guess is",cpu)

        while count >= 0:
            count += 1
            player = input("Was my too high, too low, or correct? (h/l/c): ")

            if cpu == num:
                print(f"I win in {count} guesses!")
                break
            elif player == 'h':
                # move to lower half of range
                max = cpu
            elif player == 'l':
                # move to upper half of range
                min = cpu
            cpu = min + (max - min) // 2 
            print("My guess is", cpu)
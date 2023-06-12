# Level Three
# In level three, the computer's guesses are optimized to refine each guess based on 
# whether the previous guess was too high or too low. Print how many guesses it takes 
# the computer before it correctly guesses the number.

import random

count = 0

num = int(input("Hello, I am CPU. Tell me if I my guess is too high or too low until I get your number. Enter a number between 1 and 10 for me to guess: "))
cpu = 5

min = 1
max = 11

print("My guess is",cpu)

while count >= 0:
    count += 1
    player = input("Was my too high or too low? (h/l/c): ")

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
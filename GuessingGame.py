import random
print ("this is number guessing game")

value = random.randint(1, 9)
chances = 0
print ("guess a number between 1 and 9")

while chances <5:
    enter = int( input("enter your guess"))
    if enter == value:
        print("congratulations you won")
        break
    elif enter < value:
        print ("your guess is too low guess a higher number")
    else :
        print ("your guess is too high guess a lower number")
    chances = chances+1

if not chances <5:
    print("you lose the numner is"+value)
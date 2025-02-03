from random import randint
num = randint(1,10)

guess = int(input("Guess a number between 1-10: "))

if guess == num:
    print("You got it!!!")
else:
    print("WRONGGG!!11!")
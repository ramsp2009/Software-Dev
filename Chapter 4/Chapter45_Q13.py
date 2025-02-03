from random import randint
player = 0
bot = 0
tie = 0

for i in range(5):
    throw = randint(1,3)
    if throw == 1:
        sign = "Scissors"
    if throw == 2:
        sign = "Paper"
    if throw == 3:
        sign = "Rock"
    psign = int(input("Choose rock (3), paper (2) or scissors (1): "))
    print(sign)
    if psign == 1:
        if throw == 1:
            tie = tie + 1
        if throw == 2:
            player = player+ 1
        if throw == 3:
            bot = bot + 1
    if psign == 2:
        if throw == 2:
            tie = tie + 1
        if throw == 3:
            player=player+1
        if throw == 1:
            bot = bot + 1
    if psign == 3:
        if throw == 3:
            tie = tie + 1
        if throw == 1:
            player = player+1
        if throw == 2:
            bot = bot + 1
if bot > player:
    print("Bot wins")
elif player > bot:
    print("Player wins")
elif player == bot:
    print("Tie")

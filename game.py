# SNAKE WATER GUN GAME CODE

import random

def game_winner(computer , me):
    if computer == me:
        return None          # game is tie

# all posibilities check as per computer take random choices between snake , water and gun.

    elif computer == 'snake':
        if me == 'water':
            return False    
        elif me == 'gun':
            return True
    elif computer == 'gun':
        if me == 'snake':
            return False
        elif me == 'water':
            return True
    elif computer == 'water':
        if me == 'gun':
            return False
        elif me == 'snake':
            return True
            
while(True):

    print("computer turn: snake, water & gun")

    randomnumber = random.randint(1, 3)
    # print(randomnumber)
    if randomnumber == 1:
        computer = 'snake'
    elif randomnumber == 2:
        computer = 'water'
    elif randomnumber == 3:
        computer = 'gun'

    me = input("your turn: snake, water & gun: ")

    a = game_winner(computer, me)

    print(f"computer choose {computer}")
    print(f"me choose {me}")

    if a == None:
        print("game is tie!")
    elif a == True:
        print("you win.")
    elif a == False:
        print("you loss.")
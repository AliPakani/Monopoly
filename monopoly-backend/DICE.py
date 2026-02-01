import random
import time
import os

size = os.get_terminal_size()
size = size.columns

def Roll(Username) :
    Choice = input(("Roll the dice").center(size))
    c = 0
    Dice1 = int(input())
    Dice2 = int(input())
    Move = Dice1 + Dice2
    Username["Dice"] = [Dice1, Dice2]
    print((f"You roll {Dice1} & {Dice2}").center(size))
    time.sleep(2)
    if Dice1 != Dice2 :
        return (Move, 0)
    else :
        return (Move, 1)

#Rolling a dice in JAIL
def Roll_Jail(Username) :
    c = 0
    while c < 3 :
        Choice = input(("Roll the dice").center(size))
        Dice1 = int(input())
        Dice2 = int(input())
        c += 1
        if Dice1 == Dice2:
            Username["Arrested"] = False
            Username["Position"] += Dice1 + Dice2
            return 1        
        

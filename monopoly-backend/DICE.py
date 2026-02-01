import random
from MOVE import Position

def Roll(Username) :
    Choice = input("Roll the dice")
    c = 0
    Move = 0
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    Move += Dice1 + Dice2
    Username["Position"] += Move
    Username["Dice"] = [Dice1, Dice2]
    print(f"You roll {Dice1} & {Dice2}")
    if Dice1 != Dice2 :
        return 0
    else :
        return 1

#Rolling a dice in JAIL
def Roll_Jail(Username) :
    c = 0
    while c < 3 :
        Dice1 = random.randint(1,6)
        Dice2 = random.randint(1,6)
        c += 1
        if Dice1 == Dice2:
            Username["Arrested"] = False
            Username["Position"] += Dice1 + Dice2
            Position(Username)
            return 1
    return 0
        

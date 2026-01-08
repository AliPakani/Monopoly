import random
from MOVE import Position
from PLAYER import Go_To_Jail
from BANK import Check_Rent

def Chance(Username, Number) :
    Chance = [8, 23, 37]
    if Number in Chance :
        Random = int(input())
        match Random :
            case 1 :
                Username["Position"] = 40
                print("You're now in Boardwalk")
            case 2 :
                Check_Rent(Username, 15)
            case 3 :
                Go_To_Jail(Username)
            case 4 :
                Username["Position"] = 41
                print("You're now in GO")
                Position(Username)

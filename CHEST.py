import random
from PLAYER import Deposit, Dedute, Go_To_Jail
from BANK import Check_Rent

def Community_chest(Username, Number):
    Chest = [3, 18, 34]
    if Number in Chest :
        Random = random.randint(1,4)
        match Random :
            case 1 :
                Deposit(Username, 100)
            case 2 :
                Deposit(Username, 200)
            case 3 :
                Check_Rent(Username, 100)
            case 4 :
                Go_To_Jail(Username)
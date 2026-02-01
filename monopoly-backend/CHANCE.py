import random
from MOVE import Position
from PLAYER import Bankrupt, Dedute, Deposit, Buy, Sell, Assest, Go_To_Jail
from ESTATE import Find_Owner, Find_Price, Find_Rent, Owner_Replace, Find_Estate
from BANK import Check_Balance, Check_Rent
from RAILROAD import Railroad
from COMPANY import Company_Buy, Company_Rent
import json


def Chance(Username, Number, PLAYERS):
    Chance = [8, 23, 37]
    if Number in Chance :
        Random = random.randint(1,7)
        match Random :
            case 1:
                print("Let's see what luck has for you...")
                print("-->Advance to GO (collect $200)")
                Username["Position"] = 41
                Position(Username)
            case 2:
                print("Let's see what luck has for you...")
                print("-->Advance to Boardwalk")
                Username["Position"] = 40
            case 3:
                print("Let's see what luck has for you...")
                print("-->Go to Jail")
                Go_To_Jail(Username)
            case 4:
                print("Let's see what luck has for you...")
                print("-->High-Risk investment! Roll the dice to see your fate")
                dice = random.randint(1,6)
                if dice % 2 == 0 :
                    Deposit(Username, 300)
                else :
                    Check_Rent(Username, 200)
            case 5 :
                print("Let's see what luck has for you...")
                print("-->Go Back 3 Spaces")
                Username["Position"] -= 3
            case 6 :
                print("Let's see what luck has for you...")
                print("-->Its Your Birthday!!Collect $50 and move forward 1 space")
                Username["Balance"] += 50
                Username["Position"] += 1
            case 7:
                print("Let's see what luck has for you...")
                print("-->You have been elected Chairman of the Board, Pay each player $50")
                for player in PLAYERS:
                    if player != Username:
                        Check_Rent(Username, 50)
                        Deposit(player, 50)

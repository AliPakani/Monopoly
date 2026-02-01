import random
from MOVE import Position
from PLAYER import Bankrupt, Dedute, Deposit, Buy, Sell, Assest, Go_To_Jail
from ESTATE import Find_Owner, Find_Price, Find_Rent, Owner_Replace, Find_Estate
from BANK import Check_Balance, Check_Rent
from RAILROAD import Railroad
from COMPANY import Company_Buy, Company_Rent
import json
with open("PLAYERS.json", "r",encoding="utf-8") as p :
    PLAYERS = json.load(p)
with open("CELLS.json", "r",encoding="utf-8") as c :
    CELLS = json.load(c)
def Chance(Username, Number):
    Chance = [8, 23, 37]
    if Number in Chance :
        Random = random.randint(1,10)
        match Random :
            case 1:
                print("Let's see what luck has for you...")
                print("-->Advance to GO (collect $200)")
                Username["Position"] = 1
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
                if dice% 2 == 0 :
                    Username["Balance"] += 300
                else :
                    Username["Balance"] -= 200
            case 5 :
                print("Let's see what luck has for you...")
                print("-->Advance to St.Charles Place(if you pass GO, collect $200)")
                Username["Position"] = 12
            case 6 :
                print("Let's see what luck has for you...")
                print("-->Go Back 3 Spaces")
                if Username["Position"] > 3 :         
                    Username["Position"] -= 3
            case 7 :
                print("Let's see what luck has for you...")
                print("-->Its Your Birthday!!Collect $50 and move forward 1 space")
                Username["Balance"] += 50
                Username["Position"] += 1
            case 8:
                print("Let's see what luck has for you...")
                print("-->You have been elected Chairman of the Board, Pay each player $50")
                for player in PLAYERS:
                    if player != Username:
                        Username["Balance"] -= 50
                        player["Balance"] += 50
            case 9:
                print("Let's see what luck has for you...")
                print("-->Advance to the nearest Railroad." \
                " If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled")
                Road = [6, 16, 26, 36]
                if Username["Position"] < 6 :
                    Username["Position"] = 6 
                elif Username["Position"] < 16 :
                    Username["Position"] = 16
                elif Username["Position"] <26:
                    Username["Position"] = 26
                elif Username["Position"] <36:
                    Username["Position"] = 36
                else :
                    Username["Position"] = 6
                    Username["Balance"] += 200
                Cell = CELLS[Username["Position"]]
                if Find_Owner(Cell) == "" : 
                    while True :                                  
                        Choice = input("Do you want to buy it?(Y/N)").lower().strip()
                        if not Choice :
                            print("please enter Y or N")
                            continue
                        first_character = Choice[0]
                        if first_character == 'y' :                                             #خرید
                            Amount = Find_Price(Cell)
                            if Check_Balance(Username, Amount) == 1 :
                                Buy(Username, Cell)
                                Dedute(Username, Amount)
                                Owner_Replace(Username, Cell)
                                Railroad(Username, Number, Cell)
                                break
                            else :
                                print(f"You can't buy {Cell["name"]}")    
                                break
                        elif first_character == "n" :
                            break
                        else :
                            print("invalid input!please enter Y or N")
                elif Find_Owner(Cell) != Username["Username"]:
                    Rent = Find_Rent(Cell)
                    Username["Balance"] -= Rent * 2
                    print(f"{Rent*2}$ deducted from {Username["Username"]}'s balance!")
                elif Find_Owner(Cell) == Username["Username"] :
                    print("you own the place!")
            case 10 :
                print("Let's see what luck has for you...")
                print("-->Advance token to nearest Utility." \
                " If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown. ")
                if Username["Position"] < 13 :
                    Username["Position"] = 13 
                elif Username["Position"] < 29 :
                    Username["Position"] = 29
                else :
                    Username["Position"] = 13
                while True :                                  
                    Choice = input("Do you want to buy it?(Y/N)").lower().strip()
                    if not Choice :
                        print("please enter Y or N")
                        continue
                    first_character = Choice[0]
                    if first_character == 'y' :                                             #خرید
                        Amount = Find_Price(Cell)
                        if Check_Balance(Username, Amount) == 1 :
                            Buy(Username, Cell)
                            Dedute(Username, Amount)
                            Owner_Replace(Username, Cell)
                            Company_Buy(Username, Number, Cell)
                            break
                    elif Cell["Owner"] != Username["Name"]:
                        dice = random.randint(1,6)
                        Username["Balance"] -= dice * 10
                        print(f"{dice*10 }deducted from {Username["Username"]}'s balance!")
                    elif Find_Owner(Cell) == Username["Username"] :
                        print("you own the place!")
                    elif first_character == "n" :
                        break
                    else :
                        print("invalid input!please enter Y or N")
                Position(Username)

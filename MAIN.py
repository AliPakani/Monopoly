import json
import random
from DICE import Roll, Roll_Jail
from MOVE import Position
from PLAYER import Bankrupt, Dedute, Deposit, Buy, Sell, Assest, Go_To_Jail
from ESTATE import Find_Owner, Find_Price, Find_Rent, Owner_Replace, Find_Estate
from BANK import Check_Balance, Check_Rent
from CHEST import Community_chest
from CHANCE import Chance
from JAIL import Jail
from RAILROAD import Railroad
from COMPANY import Company_Buy, Company_Rent

PLAYERS = json.load(open("PLAYERS.json"))
CELLS = json.load(open("CELLS.json"))

def check_build(Username) :
    COLOR = ["Brown", "Red", "Green", "Cyen", "Blue", "Yellow", "Orange", "Pink"]
    for color in COLOR :
        Same_Color = Same_Color_Estates(color)
        r = same_color(Username, color)
        if len(Same_Color) == len(r) :
            return 1
    return 0


def same_color(Username, color) :
    r = []
    for Estate in Username["Estate"] :
        if Estate["color"] == color :
            r.append(Estate)
    return r


def Hotel(Estate, Username) :
    global size
    COLOR = Estate["color"]
    Required_Estate = Same_Color_Estates(COLOR)
    for i in Required_Estate :
        if i["Number"] != 4 :
            print("You can't build a hotel!")
            return 0
    Choice = ""
    while Choice != "Y" and Choice != "N" :
        Choice = input("Do you want to build a hotel?(Y/N)").upper()
        try :
            if Choice == 'Y' :
                Amount = Estate["Build_Price"]
                Check = Check_Rent(Username, Amount)
                if Check == 1 :
                    for i in Required_Estate :
                        i["Rent"].pop(0)
                    print("You build a hotel succesfully!")
                else :
                    Username["Status"] = "Solvent"
                    print("You don't have enought money to build!")
        except :
            print("Invalid input! TRY AGAIN")


def House(Username) :
    if check_build(Username) == 1 :
        Buy = ''
        while Buy != "Y" and Buy != "N" :
            Buy = input("Do you want to build house?(Y/N)").upper()
            if Buy == "Y" or Buy == "N" :
                if Buy == "Y" :
                    COLOR = ""
                    Color = ["brown", "red", "green", "cyen", "blue", "yellow", "orange", "pink"]
                    while COLOR not in Color :
                        COLOR = input("Which color do you want to build in?").lower()
                        if COLOR in Color :
                            COLOR = COLOR.title()
                            break
                        else :
                            print("Invalid input! Please enter the COLOR")
                    Required_Estate = Same_Color_Estates(COLOR)
                    if Check_Ownership(Username, Required_Estate) == 1 :
                        Choice = CELLS[Estate_selection(Required_Estate)]
                        if Consecutiveness(Choice, Required_Estate) == 1 :
                            Amount = Choice["Build_Price"]
                            Check = Check_Rent(Username, Amount)
                            if Check == 1 :
                                Choice["Rent"].pop(0)
                                Choice["Number"] += 1
                                print("You build a house succesfully!")
                            else :
                                Username["Status"] = "Solvent"
                                print("You don't have enought money to build!")
                        elif Consecutiveness(Choice, Required_Estate) == 0 :
                            Hotel(Choice, Username)

            else :
                print("Invalid input! TRY AGAIN")


def Same_Color_Estates(COLOR) :
    Required = []
    for Estate in CELLS :
        if Estate["color"] == COLOR :
            Required.append(Estate)
    return Required


def Check_Ownership(Username, Required_Estate) :
    for Estate in Required_Estate :
        if Estate["Owner"] != Username["Username"] :
            print("You can't build in this color!")
            return 0
    return 1


def Estate_selection(Required_Estate) :
    Name = [Estate["name"] for Estate in Required_Estate]
    print(Name)
    Number = [x + 1 for x in range(len(Required_Estate))]
    Choice = ''
    while Choice not in Number :
        Choice = int(input(("Which Estate do you want to build in?")))
        if Choice not in Number :
            print("Invalid input! Please enter the NUMBER")
    Choice = Required_Estate[int(Choice) - 1]
    return Choice["no."]


def Consecutiveness(Choice, Required_Estate) :
    Built_Number = []
    for Estate in Required_Estate :
        Built_Number.append(Estate["Number"])
    if Choice["Number"] < 4:
        if min(Built_Number) == Choice["Number"] :
            return 1
        else :
            print("You can't build house in this Estate!")
    else :
        if len(Choice["Rent"]) == 2:
            print("Yey")
            return 0
        else :
            print("You have already built a hotel!")


def Save_Game():
    global PLAYERS, CELLS
    players_data = json.dumps(PLAYERS, ensure_ascii=False, indent=4)                        
    players_data = players_data.replace("},\n    {", "},\n\n    {")
    with open("PLAYERS.json", "w", encoding="utf-8") as f:
        f.write(players_data)
    cells_data = json.dumps(CELLS, ensure_ascii=False, indent=4)
    cells_data = cells_data.replace("},\n    {", "},\n\n    {")
    with open("CELLS.json", "w", encoding="utf-8") as f:
        f.write(cells_data)


while True :
    for Username in PLAYERS :
        if Username["Status"] == "Solvent" :
            FLAG = 0
            c = 0
            while FLAG == 0 :  
                print(f"It's {Username["Username"]}'s turn.")  
                print(f"Now you're in {Username["Position"]}")
                if Username["Arrested"] :
                    Jail(Username)
                else :
                    if Roll(Username) == 0 :
                        FLAG = 1
                    else :
                        c += 1
                        if c == 3 :
                            Go_To_Jail(Username)
                            break
                    Position(Username)
                    Number = Username["Position"]                                       #شماره خانه کنونی بازیکن
                    Cell = CELLS[Number]
                    print(f"You're in {Cell["name"]}")                                            #اطلاعات خانه کنونی بازیکن به صورت دیکشنری
                    if Find_Price(Cell) == 0 :                                          #خانه های غیر قابل خرید
                        if Find_Rent(Cell) != 0:                                        
                            Amount = Find_Rent(Cell)
                            Dedute(Username, Amount)
                        Community_chest(Username, Number)
                        Chance(Username, Number, PLAYERS)
                        if Number == 31 :
                            Go_To_Jail(Username, Number, CELLS, PLAYERS)
                    else :                                                              #خانه های قابل خرید
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
                                        Company_Buy(Username, Number, Cell)
                                    else :
                                        print(f"You can't buy {Cell["name"]}")    
                                    break
                                elif first_character == "n" :
                                    break
                                else :
                                    print("invalid input!please enter Y or N")           
                        else :                                                             #اجاره
                            Owner = Find_Owner(Cell)
                            for i in PLAYERS:
                                if i["Username"] == Owner :                                #اطلاعات مالک به صورت دیکشنری
                                    Owner = i
                                    break
                            if Username["Username"] == Owner["Username"] :
                                print("You're the owner!")
                            else :
                                Company = Company_Rent(Username, Owner, Number)
                                if Company > 0 :
                                    Amount = Company
                                else :
                                    Amount = Find_Rent(Cell)
                                if Check_Balance(Username, Amount) == 1 :
                                    Dedute(Username, Amount)
                                    Deposit(Owner, Amount)
                                else :
                                    Can_Pay = Check_Rent(Username, Amount)
                                    if Can_Pay == 1 :
                                        Deposit(Owner, Amount)
    while True :
        Save = input("Do you want to save game?(Y/N)").lower().strip()
        if not Save:
            print("please enter Y or N")
            continue
        first_character = Save[0]
        if first_character == "y":
            Save_Game()
            break
        elif first_character == "n":
            break
        else:
            print("invalid input!please enter Y or N")                                    #خروج از بازی
    while True:
        Exit = input("Do you want to end game?(Y/N)").lower().strip()
        if not Exit:
            print("please enter Y or N")
            continue
        first_character = Exit[0]
        if first_character == "y":
            break
        elif first_character == "n":
            break
        else:
            print("invalid input!please enter Y or N")
    if first_character == "n" :
        break
    

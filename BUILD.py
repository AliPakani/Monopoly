import json
from BANK import Check_Rent
from PLAYER import Dedute, Deposit, Sell
from ESTATE import Find_Estate

CELLS = json.load(open("CELLS.json"))

def check_build(Username) :
    COLOR = ["brown", "red", "green", "cyen", "blue", "yellow", "orange", "pink"]
    for color in COLOR :
        Same_Color = Same_Color_Estates(color, CELLS)
        r = same_color(Username, color)
        if Same_Color == r :
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
    while True :
        Choice = input("Do you want to build a hotel?(Y/N)").lower()
        first_character = Choice[0]
        if not Choice :
            print("Invalid input! TRY AGAIN")
            try :
                if first_character == 'y' :
                    Amount = Estate["Build_Price"]
                    Check = Check_Rent(Username, Amount)
                    if Check == 1 :
                        for i in Required_Estate :
                            i["Rent"].pop(0)
                        print("You build a hotel succesfully!")
                    else :
                        Username["Status"] = "Solvent"
                        print("You don't have enought money to build!")
                if first_character == 'n' :
                    return
            except :
                print("Invalid input! TRY AGAIN")


def House(Username, CELLS) :
    if check_build(Username) == 1 :
        while True :
            Buy = input("Do you want to build house?(Y/N)").lower()
            first_character = Buy[0]
            if not Buy :
                print("Invalid input! TRY AGAIN")
                continue
            elif first_character == "y" :
                while True :
                    COLOR = input("Which color do you want to build in?").lower()
                    Color = ["brown", "red", "green", "cyen", "blue", "yellow", "orange", "pink"]
                    if not COLOR :
                        print("Invalid input! TRY AGAIN")
                        continue
                    if COLOR not in Color :
                        print("Please enter a valid color")
                        continue
                    if COLOR in Color :  
                        Required_Estate = Same_Color_Estates(COLOR, CELLS)
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
            elif first_character == "n" :
                return 
            else :
               print("Invalid input! TRY AGAIN") 
def Same_Color_Estates(COLOR, CELLS) :
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
        Choice = int(input("Which Estate do you want to build in?"))
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
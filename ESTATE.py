import json

CELLS = json.load(open("CELLS.json"))

def Find_Owner(Estate) :
    Owner = Estate["Owner"]
    return Owner


def Find_Price(Estate) :
    Price = Estate["Price"]
    return Price


def Find_Rent(Estate) :
    Rent = Estate["Rent"][0]
    return Rent


def Owner_Replace(Username, Estate) :
    Estate["Owner"] = Username["Username"]
    print(f"Now {Username["Username"]} is the owner of {Estate["name"]}")


def Find_Estate(EstateList) :                                               #با استفاده از شماره یک خانه اطلاعات دیکشنری مربوط به آن خانه را به دست می آورد
    global CELLS
    AssestList = []
    for num in EstateList :
        AssestList.append(CELLS[num])
    return AssestList
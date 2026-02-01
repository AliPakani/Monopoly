from ESTATE import Find_Price
import time 
import os
from BOARD import animated_move

size = os.get_terminal_size()
size = size.columns

def Lost_Estate(Username, Owner, CELLS) :
    if Owner != "" :
        for Estate in Username["Estate"] :
            for Target in CELLS :
                if Estate["name"] == Target["name"] :
                    Target["Owner"] = Owner["Username"]
                    Owner["Estate"].append(Target)
    Username["Estate"].clear()


def Bankrupt(Username) :
    Username["Status"] = "Bankrupt"
    Username["Balance"] = 0
    print(f"Hey {Username['Username']}! You got bankrupt!".center(size))
    time.sleep(2)

def Dedute(Username, amount) :
    if Username["Balance"] - amount > 0 :
        Username["Balance"] -= amount
        print((f"{amount}$ deducted from {Username["Username"]}'s balance!").center(size))
        time.sleep(2)
    else :
        Username["Balance"] = 0



def Deposit(Username, Amount) :
    Username["Balance"] += Amount
    print(f"{Amount}$ added to {Username["Username"]}'s balance!".center(size))
    time.sleep(2)


def Buy(Username, Estate) :
    Username["Estate"].append(Estate)
    Estate["Owner"] = Username["Username"]

def Sell(Username, Estate) :
    I = Username["Estate"].index(Estate)
    Username["Estate"].pop(I)


def Assest(Username) :                                      #جمغ کل دارایی ها
    Sum = 0
    for Estate in Username["Estate"] :
        Sum += Find_Price(Estate)
    return Sum + Username["Balance"]


def Go_To_Jail(Username, CELLS, PLAYERS) :
    animated_move(Username, 11 - Username["Position"], CELLS, PLAYERS)
    Username["Arrested"] = True
    print(("You went to jail!").center(size))
    time.sleep(2)

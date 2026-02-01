import json
from PLAYER import Bankrupt, Dedute, Deposit, Buy, Sell, Assest
from ESTATE import Find_Price, Find_Estate
import os

size = os.get_terminal_size()
size = size.columns


def Check_Balance(Username, amount) :
    if Username["Balance"] >= amount :
        return 1
    else :
        return 0

def Check_Assest(Username, AssestList) :                    #جمع قیمت اموال انتخاب شده
    Sum = 0
    for Estate in AssestList :
        Sum += Find_Price(Estate)
        print(Sum)
    return Sum


def same_owner(Username, CELLS) :
    i = []
    for Estate in CELLS :
        if Estate["Owner"] == Username["Username"] :
            i.append(Estate["no."])
    return i


def Check_Rent(Username, Amount, CELLS):
    if Check_Balance(Username, Amount) == 1 :
        Dedute(Username, Amount)
        Username["Arrested"] = False
        return 1
    else :
        if Assest(Username) // 2 > Amount :                             
            AssestList = []
            Debt = 0
            while Debt // 2 < Amount : 
                Debt = Check_Assest(Username, AssestList)
                print(("YOU ARE THE OWNER OF THESE ESTATES:", same_owner(Username, CELLS)).center(size))
                EstateList = list(map(int, input(("Which estate do you want to sell?").center(size)).split()))
                try :
                    AssestList = Find_Estate(EstateList)
                except Exception as e :
                    print(("Invalid input! Please enter the NUMBER").center(size))
            Deposit(Username, Debt // 2)
            for Estate in AssestList :                              
                Sell(Username, Estate)
            Dedute(Username, Amount)
            Username["Arrested"] = False
            return 1
        else :
            Bankrupt(Username)
            return 0

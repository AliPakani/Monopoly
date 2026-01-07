import json
from PLAYER import Bankrupt, Dedute, Deposit, Buy, Sell, Assest
from ESTATE import Find_Price, Find_Estate


def Check_Balance(Username, amount) :
    if Username["Balance"] >= amount :
        return 1
    else :
        return 0


def Check_Assest(Username, AssestList) :                    #جمع قیمت اموال انتخاب شده
    Sum = 0
    for Estate in AssestList :
        Sum += Find_Price(Estate)
    return Sum


def Check_Rent(Username, Amount):
    if Check_Balance(Username, Amount) == 1 :
        Dedute(Username, Amount)
        Username["Arrested"] = False
        return 1
    else :
        if Assest(Username) // 2 > Amount :                             
            AssestList = []
            Debt = 0
            while Debt < Amount :                                  
                Debt = Check_Assest(Username, AssestList)
                EstateList = list(map(int, input("Which estate do you want to sell?")))
                AssestList = Find_Estate(EstateList)
            Deposit(Username, Debt)
            for Estate in AssestList :                              
                Sell(Username, Estate)
                Dedute(Username, Amount)
            Username["Arrested"] = False
            return 1
        else :
            Bankrupt(Username)
            return 0
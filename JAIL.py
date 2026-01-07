from DICE import Roll, Roll_Jail
from BANK import Check_Rent

def Jail(Username) :
    Choice = input("Do you want to pay 50$?(Y/N)")
    if Choice == "Y" :
        Check_Rent(Username, 50)
    else :
        Status = Roll_Jail(Username)
        if Status == 0 :
            Check_Rent(Username, 50)
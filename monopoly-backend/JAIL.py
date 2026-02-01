from DICE import Roll, Roll_Jail
from BANK import Check_Rent

def Jail(Username) :
    while True : 
        Choice = input("Do you want to pay 50$?(Y/N)").lower().strip()
        if not Choice :
            print("please enter Y or N")
            continue
        first_character = Choice[0]
        if first_character == "y" :
            Check_Rent(Username, 50)
            return
        elif first_character == "n"  :
            Status = Roll_Jail(Username)
            if Status == 0 :
                Check_Rent(Username, 50)
            return
        else:
            print("Invalid input! TRY AGAIN")
    

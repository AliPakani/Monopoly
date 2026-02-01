from DICE import Roll, Roll_Jail
from BANK import Check_Rent
import os

size = os.get_terminal_size()
size = size.columns


def Jail(Username, CELLS) :
    global size
    while True : 
        Choice = input("Do you want to pay 50$?(Y/N)".center(size)).lower().strip()
        if not Choice :
            print("please enter Y or N".center(size))
            continue
        first_character = Choice[0]
        if first_character == "y" :
            Check_Rent(Username, 50, CELLS)
            return
        elif first_character == "n"  :
            Status = Roll_Jail(Username)
            if Status != 1 :
                Check_Rent(Username, 50, CELLS)
            return
        else:
            print("Invalid input! TRY AGAIN".center(size))
    

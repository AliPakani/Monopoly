import random
from PLAYER import Deposit, Go_To_Jail
from BANK import Check_Rent
import os
import time
from BOARD import animated_move


size = os.get_terminal_size()
size = size.columns


def Chance(Username, Number, PLAYERS, CELLS):
    Chance = [8, 23, 37]
    if Number in Chance :
        Random = random.randint(1,7)
        match Random :
            case 1:
                print("Let's see what luck has for you...".center(size))
                print("-->Advance to GO (collect $200)".center(size))
                time.sleep(2)
                animated_move(Username, 41 - Username["Position"], CELLS, PLAYERS)
            case 2:
                print("Let's see what luck has for you...".center(size))
                print("-->Advance to Boardwalk".center(size))
                time.sleep(2)
                animated_move(Username, 40 - Username["Position"], CELLS, PLAYERS)
            case 3:
                print("Let's see what luck has for you...".center(size))
                print("-->Go to Jail".center(size))
                time.sleep(2)
                Go_To_Jail(Username, CELLS, PLAYERS)
            case 4:
                print("Let's see what luck has for you...".center(size))
                print("-->High-Risk investment! Roll the dice to see your fate".center(size))
                time.sleep(2)
                dice = random.randint(1,6)
                if dice % 2 == 0 :
                    Deposit(Username, 300)
                    time.sleep(2)
                else :
                    Check_Rent(Username, 200)
                    time.sleep(2)
            case 5 :
                print("Let's see what luck has for you...".center(size))
                print("-->Go Back 3 Spaces".center(size))
                time.sleep(2)
                animated_move(Username, -3, CELLS, PLAYERS)
            case 6 :
                print("Let's see what luck has for you...".center(size))
                print("-->Its Your Birthday!!Collect $50 and move forward 1 space".center(size))
                Username["Balance"] += 50
                time.sleep(2)
                animated_move(Username, 1, CELLS, PLAYERS)
            case 7:
                print("Let's see what luck has for you...".center(size))
                print("-->You have been elected Chairman of the Board, Pay each player $50".center(size))
                for player in PLAYERS:
                    if player != Username:
                        Check_Rent(Username, 50)
                        Deposit(player, 50)
                        time.sleep(2)

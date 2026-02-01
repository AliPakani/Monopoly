import os
import time


size = os.get_terminal_size()
size = size.columns

def board_structure(Username, CELLS, PLAYERS) :
    os.system('cls' if os.name == 'nt' else 'clear')
    print(("╔" + 10 * "═════╦" + "═════╗").center(size))
    #21 to 30
    alias = "║"
    position = "║"
    for i in range(21, 32):
        alias += " " + CELLS[i]["alias"] + " ║" 
        C1 = 1
        for j in PLAYERS : 
            if j["Position"] == i :
                position += " " + "PL" + str(C1) + " ║"
                break
            C1 += 1
        else  :
            position += " " + "___" + " ║"
    print((alias).center(size))
    print((position).center(size))
    print(("╠" + "═════╬" + 8 * "═════╩" + "═════╬" + "═════" + "╣").center(size))
    #body
    alias = "║"
    position = "║"
    c = 12
    for i in range(20, 11, -1) :
        C1 = 1
        C2 = 1
        for j in PLAYERS : 
            if j["Position"] == i :
                player1 = "PL" + str(C1)
                break
            C1 += 1
        else :
            player1 = "___"

        for j in PLAYERS : 
            if j["Position"] == i + c :
                player2 = "PL" + str(C2)
                break
            C2 += 1
        else :
            player2 = "___"
            
        if i == 19 :
            print(("║" + f" {CELLS[i]["alias"]} ║" + "GAME STATUS".center(53) + f"║ {CELLS[i + c]["alias"]} " + "║").center(size))
            print(("║" + f" {player1} ║" + f"{PLAYERS[0]["Username"]}: {PLAYERS[0]["Balance"]}$".center(53) + f"║ {player2} " + "║").center(size))
            print(("╠" + "═════╣" + f"{PLAYERS[1]["Username"]}: {PLAYERS[1]["Balance"]}$".center(53) + "╠═════" + "╣").center(size))
        elif i == 18 :
            print(("║" + f" {CELLS[i]["alias"]} ║" + f"{PLAYERS[2]["Username"]}: {PLAYERS[2]["Balance"]}$".center(53) + f"║ {CELLS[i + c]["alias"]} " + "║").center(size))
            print(("║" + f" {player1} ║" + f"{PLAYERS[3]["Username"]}: {PLAYERS[3]["Balance"]}$".center(53) + f"║ {player2} " + "║").center(size))
        elif i == 16 :
            print(("║" + f" {CELLS[i]["alias"]} ║" + f"It's {Username["Username"]}'s turn!".center(53) + f"║ {CELLS[i + c]["alias"]} " + "║").center(size))
            print(("║" + f" {player1} ║" + " " * 53 + f"║ {player2} " + "║").center(size))
        else :
            print(("║" + f" {CELLS[i]["alias"]} ║" + " " * 53 + f"║ {CELLS[i + c]["alias"]} " + "║").center(size))
            print(("║" + f" {player1} ║" + " " * 53 + f"║ {player2} " + "║").center(size))
        if i != 12 and i != 19:
            print(("╠" + "═════╣" + " " * 53 + "╠═════" + "╣").center(size))
        c += 2
    #1 to 11
    print(("╠" + "═════╬" + 8 * "═════╦" + "═════╬" + "═════" + "╣").center(size))
    alias = "║"
    position = "║"
    for i in range(11, 0, -1):
        alias += " " + CELLS[i]["alias"] + " ║" 
        C1 = 1
        for j in PLAYERS : 
            if j["Position"] == i :
                position += " " + "PL" + str(C1) + " ║"
                break
            C1 += 1
        else  :
            position += " " + "___" + " ║"
    print((alias).center(size))
    print((position).center(size))
    print(("╚" + 10 * "═════╩" + "═════╝").center(size))
    print()


def animated_move(Username, Move, CELLS, PLAYERS) :
    if Move >= 0 :
        for i in range(Move) :
            Username["Position"] += 1
            if Username["Position"] > 40 :
                Username["Position"] %= 40
                # Deposit(Username, 200)
                Username["Balance"] += 200
            board_structure(Username, CELLS, PLAYERS)
            time.sleep(0.5)
    else :
        for i in range(0, Move, -1) :
            Username["Position"] -= 1
            if Username["Position"] == 0:
                Username["Position"] = 40
            board_structure(Username, CELLS, PLAYERS)
            time.sleep(0.5)
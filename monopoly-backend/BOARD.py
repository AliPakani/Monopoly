import os
import time
import rich
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.align import Align
console = Console()

size = os.get_terminal_size()
size = size.columns

Cell_style= {
    "brown":     "bold black on #8B5A2B",
    "cyen":      "bold black on #87CEFA",
    "pink":      "bold black on #FF69B4",
    "orange":    "bold black on #FFA500",
    "red":       "bold white on #E53935",
    "yellow":    "bold black on #FDD835",
    "green":     "bold white on #43A047",
    "blue":      "bold white on #1E88E5",
}

def cells_color(cell):
    alias = cell["alias"]
    c = cell["color"]              
    c = c.strip().lower() 
    style = Cell_style.get(c, "bold white on #2B2F36")
    return f"[{style}]{alias}[/]"
    
def board_structure(Username, CELLS, PLAYERS) :
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(Align.center("[yellow]╔[/yellow]" + 10 * "[yellow]═════╦[/yellow]" + "[yellow]═════╗[/yellow]"))
    #21 to 30
    alias = "[yellow]║[/yellow]"
    position = "[yellow]║[/yellow]"
    for i in range(21, 32):
        alias += " " + cells_color(CELLS[i]) + " [yellow]║[/yellow]" 
        C1 = 1
        for j in PLAYERS : 
            if j["Position"] == i :
                position += " " + "[bold cyan]PL[/bold cyan]" + str(C1) + " [yellow]║[/yellow]"
                break
            C1 += 1
        else  :
            position += " " + "___" + " [yellow]║[/yellow]"
    console.print(Align.center(alias))        
    console.print(Align.center(position))
    console.print(Align.center("[yellow]╠[/yellow]" + "[yellow]═════╬[/yellow]" + 8 * "[yellow]═════╩[/yellow]" + "[yellow]═════╬[/yellow]" + "[yellow]═════[/yellow]" + "[yellow]╣[/yellow]"))
    #body
   
    alias = "[yellow]║[/yellow]"
    position = "[yellow]║[/yellow]"
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
            console.print(Align.center("[yellow]║[/yellow]" + f" {cells_color(CELLS[i])} [yellow]║[/yellow]" + "GAME STATUS".center(53) + f"[yellow]║[/yellow] {cells_color(CELLS[i + c])} " + "[yellow]║[/yellow]"))
            console.print(Align.center("[yellow]║[/yellow]" + f" {player1} [yellow]║[/yellow]" + f"{PLAYERS[0]["Username"]}: {PLAYERS[0]["Balance"]}$".center(53) + f"[yellow]║[/yellow] {player2} " + "[yellow]║[/yellow]"))
            console.print(Align.center("[yellow]╠[/yellow]" + "[yellow]═════╣[/yellow]" + f"{PLAYERS[1]["Username"]}: {PLAYERS[1]["Balance"]}$".center(53) + "[yellow]╠═════[/yellow]" + "[yellow]╣[/yellow]"))
        elif i == 18 :
            console.print(Align.center("[yellow]║[/yellow]" + f" {cells_color(CELLS[i])} [yellow]║[/yellow]" + f"{PLAYERS[2]["Username"]}: {PLAYERS[2]["Balance"]}$".center(53) + f"[yellow]║[/yellow] {cells_color(CELLS[i + c])} " + "[yellow]║[/yellow]"))
            console.print(Align.center("[yellow]║[/yellow]" + f" {player1} [yellow]║[/yellow]" + f"{PLAYERS[3]["Username"]}: {PLAYERS[3]["Balance"]}$".center(53) + f"[yellow]║[/yellow] {player2} " + "[yellow]║[/yellow]"))
        elif i == 16 :
            console.print(Align.center("[yellow]║[/yellow]" + f" {cells_color(CELLS[i])} [yellow]║[/yellow]" + f"It's {Username["Username"]}'s turn!".center(53) + f"[yellow]║[/yellow] {cells_color(CELLS[i + c])} " + "[yellow]║[/yellow]"))
            console.print(Align.center("[yellow]║[/yellow]" + f" {player1} [yellow]║[/yellow]" + " " * 53 + f"[yellow]║[/yellow] {player2} " + "[yellow]║[/yellow]"))
        else :
            console.print(Align.center("[yellow]║[/yellow]" + f" {cells_color(CELLS[i])} [yellow]║[/yellow]" + " " * 53 + f"[yellow]║[/yellow] {cells_color(CELLS[i + c])} " + "[yellow]║[/yellow]"))
            console.print(Align.center("[yellow]║[/yellow]" + f" {player1} [yellow]║[/yellow]" + " " * 53 + f"[yellow]║[/yellow] {player2} " + "[yellow]║[/yellow]"))
        if i != 12 and i != 19:
            console.print(Align.center("[yellow]╠[/yellow]" + "[yellow]═════╣[/yellow]" + " " * 53 + "[yellow]╠═════[/yellow]" + "[yellow]╣[/yellow]"))
        c += 2
    #1 to 11
    console.print(Align.center("[yellow]╠[/yellow]" + "[yellow]═════╬[/yellow]" + 8 * "[yellow]═════╦[/yellow]" + "[yellow]═════╬[/yellow]" + "[yellow]═════[/yellow]" + "[yellow]╣[/yellow]"))
    alias = "[yellow]║[/yellow]"
    position = "[yellow]║[/yellow]"
    for i in range(11, 0, -1):
        alias += " " + cells_color(CELLS[i]) + " [yellow]║[/yellow]"
        C1 = 1
        for j in PLAYERS : 
            if j["Position"] == i :
                position += " " + "PL" + str(C1) + " [yellow]║[/yellow]"
                break
            C1 += 1
        else  :
            position += " " + "___" + " [yellow]║[/yellow]"
    console.print(Align.center(alias))
    console.print(Align.center(position))
    console.print(Align.center("[yellow]╚[/yellow]" + 10 * "[yellow]═════╩[/yellow]" + "[yellow]═════╝[/yellow]"))
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

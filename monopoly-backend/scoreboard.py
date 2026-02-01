import json
import os
import re
import keyboard  
import rich    
from rich import print
from rich import inspect
from time import sleep
from rich.progress import track
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.align import Align
console = Console()


CELLS = json.load(open("CELLS.json"))
FILE_PATH = "PLAYERS.json"
scoreboard_file = "Scoreboard.json"

def exist_s():
    if not os.path.exists(scoreboard_file):
        with open(scoreboard_file, "w") as f:
            f.write("[]")
        return
    

def load_score_leaderboard():
    exist_s()
    if not os.path.exists(scoreboard_file):
        return []
    with open(scoreboard_file, "r") as f:
        return json.load(f)
   

def result_score_leaderboard(lead_data):
    results= load_score_leaderboard()
    number=len(results)+1

    def check(i):
        if i < len(lead_data):
            return lead_data[i]
        else:
            return None
        
    result={
        "save": number,
        "Rank1": check(0),
        "Rank2": check(1),
        "Rank3": check(2),
        "Rank4": check(3),
    }
    results.append(result)
    with open(scoreboard_file, "w") as f:
        json.dump(results, f, indent=4)


def load_players():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []


def save_players(players):
    with open(FILE_PATH, "w") as f:
        json.dump(players, f, indent=4)


def Find_Price(Estate) :
    Price = Estate["Price"]
    return Price


def Estate_value(Username) :                                   
    Sum = 0
    for Estate in Username["Estate"] :
        Sum += Find_Price(Estate) 
    return Sum 


def Railroadـvalue(Username):
    Sum = 0
    for Railroad in Username["Railroad"] :
        Sum += Find_Price(Railroad) 
    return Sum 


def company_value(Username):
    Sum = 0
    for Company in Username["Company"] :
        Sum += Find_Price(Company) 
    return Sum

def total_value(Username):
    return company_value(Username)+ Railroadـvalue(Username)+Estate_value(Username)+ Balance(Username)


def Balance(Username):
    value = Username.get("Balance", 0)
    if value is None or value == "":
        value = 0
    return int(value)


def Property_count(Username):
    len_p = len(Username.get("Estate", [])) + len(Username.get("Company", [])) + len(Username.get("Railroad", []))
    return len_p

 
def estate_count(Username):
    len_estate=len(Username.get("Estate", []))
    return len_estate


def Status(Username):
    st= Username["Status"]
    return st


def score_leaderboard():
    usernames = load_players()
    lead_data=[]
    for Username in usernames:
        lead_data.append({
            "Username": Username["Username"],
            "Balance": Balance(Username),
            "EstateCount": estate_count(Username),
            "PropertyCount": Property_count(Username),
            "EstateValue": Estate_value(Username),
            "RailroadValue": Railroadـvalue(Username),
            "CompanyValue": company_value(Username),
            "TotalAssets": total_value(Username),
            "Status": Status(Username),
        })

    lead_data.sort(key=lambda player: (player["TotalAssets"], player["PropertyCount"], player["Balance"]), reverse=True)
    result_score_leaderboard(lead_data)


    table = Table(title="[bold cyan]Leaderboard[/bold cyan]", box=box.ROUNDED , header_style="bold cyan")
    table.add_column("Rank", justify="right",style="magenta" )
    table.add_column("Username",style="cyan")
    table.add_column("Balance", justify="right",style="magenta")
    table.add_column("Estate Count", justify="right",style="magenta")
    table.add_column("Estate Value", justify="right",style="magenta")
    table.add_column("Railroad Value", justify="right",style="magenta")
    table.add_column("Company Value", justify="right",style="magenta")
    table.add_column("Total Assets", justify="right",style="magenta")
    table.add_column("Status", style="cyan")

    for index, data in enumerate(lead_data, start=1):
        table.add_row(
            str(index),
            data["Username"],
            str(data["Balance"]),
            str(data["EstateCount"]),
            str(data["EstateValue"]),
            str(data["RailroadValue"]),
            str(data["CompanyValue"]),
            str(data["TotalAssets"]),
            data["Status"]

        )
        

    
    return console.print(Align.center(table))







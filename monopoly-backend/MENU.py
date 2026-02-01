import json
import os
import re
import uuid
import bcrypt
import keyboard  
import time
import winsound 


import rich    
from rich import print
from rich import inspect
from time import sleep
from rich.progress import track
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich import box
from MAIN import Main

console = Console()
DARK_BLUE = "#000080"    
COLOR_GOLD = "gold1"     
GREY = "grey74"          
SKY_BLUE = "sky_blue1"   
ERROR_RED = "red"
SUCCESS_GREEN = "chartreuse3"

CELLS = json.load(open("CELLS.json"))
FILE_PATH = "PLAYERS.json"
scoreboard_file = "Scoreboard.json"
ready_players = []


MONOPOLY_LOGO = """
  ███╗   ███╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  ██████╗ ██╗  ██╗   ██╗
  ████╗ ████║██╔═══██╗████╗  ██║██╔═══██╗██╔══██╗██╔═══██╗██║  ╚██╗ ██╔╝
  ██╔████╔██║██║   ██║██╔██╗ ██║██║   ██║██████╔╝██║   ██║██║   ╚████╔╝ 
██║╚██╔╝██║██║   ██║██║╚██╗██║██║   ██║██╔═══╝ ██║   ██║██║    ╚██╔╝  
██║ ╚═╝ ██║╚██████╔╝██║ ╚████║╚██████╔╝██║     ╚██████╔╝███████╗██║   
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝      ╚═════╝ ╚══════╝╚═╝   
"""

def get_logo_text():
    return Text(MONOPOLY_LOGO, style=f"{COLOR_GOLD}", justify="center")


def create_menu_panel(content_group, title_text):
    
    return Panel(
        content_group,
        border_style=f"bold {COLOR_GOLD}",
        title=f"[bold {DARK_BLUE}] {title_text} [/]", 
        title_align="center",
        padding=(1, 4),
        expand=False,
        width=35,
        height=13
    )

def show_message(title, message, color=GREY, sleep_time=2):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    console.print(Align.center(get_logo_text()))
    console.print(Text("\n"))

    content = Group(
        Text("\n"),
        Align.center(Text(message, style=color)),
        Text("\n")
    )
    console.print(Align.center(create_menu_panel(content, title)))
    time.sleep(sleep_time)


def load_players():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []

def save_players(players):
    with open(FILE_PATH, "w") as f:
        json.dump(players, f, indent=4)

def check_email_signup(email):
    players = load_players()
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(pattern, email):
        return False, "(；￣Д￣)？Invalid email format."

    if email in [player["Email"] for player in players]:
        return False, "This email is already registered"

    return True, "Email accepted."

def check_pass(password):
   if len(password) <= 8:
      return False, "┐(ﾟ～ﾟ)┌ Password must be longer than 8 characters"
   if " " in password:
      return False, "┐(-。-;)┌ The password must not contain spaces"
   if not re.search(r"[!@#$%^&*]", password):
      return False, "(@_@;)The password must contain at least one of these characters: ! @ # $ % ^ & *"
   if not re.search(r"\d", password):
      return False, "(?_?)The password must contain at least one number"
   return True, "(^-^; Password accepted"

def start_game_logic():
    os.system('cls' if os.name == 'nt' else 'clear')
    i = Main()
    score_leaderboard()
    time.sleep(20)
    if i == 0 :
      if os.path.exists(FILE_PATH):
          os.remove(FILE_PATH)
      if os.path.exists(scoreboard_file):
          os.remove(scoreboard_file)   
    ready_players.clear()
def signup():

    try:
        if keyboard.is_pressed("enter"):
            input()
    except:
        pass


    os.system('cls' if os.name == 'nt' else 'clear')
    
    players = load_players()

    if len(players) >= 4:
        show_message("ERROR", "Maximum player limit reached (4).", ERROR_RED)
        input("Press Enter to continue...")
        return

    username = ""
    while not username:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(get_logo_text()))
        
        content = Group(
            Align.center(Text("Step 1/3: Enter Username", style=GREY)),
            Text("\n")
        )
        console.print(Align.center(create_menu_panel(content, "SIGN UP"))) 
        username = console.input("[bold blue]Enter username: [/bold blue]").strip()
        if username == " ":
            username = ""

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(get_logo_text()))

        content = Group(
            Align.center(Text(f"User: {username}", style=DARK_BLUE)),
            Align.center(Text("Step 2/3: Enter Email", style=GREY)),
            Text("\n")
        )
        console.print(Align.center(create_menu_panel(content, "SIGN UP")))  
        
        email=console.input("[bold blue]Enter email: [/bold blue]").strip()
        valid, msg = check_email_signup(email)
        if valid: break
        show_message("INVALID EMAIL", msg, ERROR_RED)
            

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(get_logo_text()))

        content = Group(
            Align.center(Text(f"User: {username}", style=DARK_BLUE)),
            Align.center(Text("Step 3/3: Enter Password", style=GREY)),
            Text("\n")
        )
        console.print(Align.center(create_menu_panel(content, "SIGN UP")))
        password=console.input("[bold blue]Enter password: [/bold blue]").strip()
        valid, msg = check_pass(password)
        if valid: break
        show_message("WEAK PASSWORD", msg, ERROR_RED)

    unique_id = str(uuid.uuid4())
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)
    f_password = hashed_bytes.decode('utf-8')

    new_player = {
        "id": unique_id,
        "Username": username,
        "Email": email,
        "Password": f_password,
        "Position": 1,
        "Balance": 1500,
        "Status":"Solvent",
        "Arrested": False,
        "Estate": [],
        "Railroad": [],
        "Company": [],
        "Dice": []
    }

    players.append(new_player)
    save_players(players)

    print(f"[yellow]Player {username} registered successfully![/yellow]")
    console.input("[bold yellow]Press Enter to continue...[/bold yellow]") 

def login():

    os.system('cls' if os.name == 'nt' else 'clear')     

    content = Group(
        Align.center(Text("Enter your credentials below", style=GREY)),
        Text("\n")
    )
    console.print(Align.center(create_menu_panel(content, "LOGIN")))

    os.system('cls' if os.name == 'nt' else 'clear')
    
    players = load_players() 
    username_input = ""
    while not username_input:
        os.system('cls' if os.name == 'nt' else 'clear') 
        console.print(Align.center(get_logo_text()))
        content = Group(
            Align.center(Text("Step 1/2: Enter Username", style=GREY)),
            Text("\n")
        )
        console.print(Align.center(create_menu_panel(content, "LOGIN")))   
        username_input = console.input("[bold blue]Enter username: [/bold blue]").strip()
        if username_input == " ":
            username_input = ""
    password_input = ""
    while not password_input:
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(get_logo_text()))
        content = Group(
            Align.center(Text("Step 2/2: Enter Password", style=GREY)),
            Text("\n")
        )
        console.print(Align.center(create_menu_panel(content, "LOGIN")))
        password_input = console.input("[bold blue]Enter password: [/bold blue]").strip()
        if password_input == " ":
            password_input = ""

    found_user = None
    for player in players:
        if player.get('Username') == username_input:
            found_user = player
            break

    if found_user is None:
        show_message("ERROR", "User not found!", ERROR_RED)
        return None  

    input_bytes = password_input.encode('utf-8')
    stored_hash_bytes = found_user.get('Password', '').encode('utf-8')

    if bcrypt.checkpw(password_input.encode('utf-8'), found_user.get('Password', '').encode('utf-8')):    
        if username_input not in ready_players:
            if len(ready_players) < 4:
                ready_players.append(username_input)
                show_message("WELCOME", f"Welcome back, {username_input}!", SUCCESS_GREEN)
            else:
                show_message("LOBBY FULL", "Lobby is full!", ERROR_RED)
        else:
            show_message("INFO", "Already logged in.", SKY_BLUE)
        return found_user 
    else:
        show_message("ERROR", "Incorrect password!", ERROR_RED)
        return None

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
        "Game": number,
        "Rank1": check(0),
        "Rank2": check(1),
        "Rank3": check(2),
        "Rank4": check(3),
    }
    results.append(result)
    with open(scoreboard_file, "w") as f:
        json.dump(results, f, indent=4)

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

    table = Table(title="[bold cyan]Leaderboard[/bold cyan]", box=box.ROUNDED)
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

    console.print(table)
    return lead_data

def interactive_menu(title_str, options):
    
    selected_index = 0
    
    time.sleep(0.2) 

    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        console.print(Align.center(get_logo_text()))
        menu_items = []
        
        for i, option in enumerate(options):
            if i == selected_index:
                item = Panel(
                    Align.center(Text(option, style=f"bold {COLOR_GOLD}")), 
                    border_style=f"bold {DARK_BLUE}",
                    expand=False,
                    padding=(0, 4) 
                )
            else:
                item = Text(option, style=f"{GREY}")

            menu_items.append(Align.center(item))
            if i != selected_index:
                menu_items.append(Text(" "))

        if ready_players:
            menu_items.append(Text("\n"))
            menu_items.append(Align.center(Text(f"Lobby: {len(ready_players)}/4 {ready_players}", style=SKY_BLUE)))

        final_content = Group(*menu_items)
        
        menu_panel = create_menu_panel(final_content, title_str)
        
        console.print(Align.center(menu_panel))
        
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            
            should_play_beep = False
            if event.name == 'esc':
                pause_menu()
            if event.name == 'up':
                new_index = (selected_index - 1) % len(options)
                if new_index != selected_index:
                    selected_index = new_index
                    should_play_beep = True
            elif event.name == 'down':
                new_index = (selected_index + 1) % len(options)
                if new_index != selected_index:
                    selected_index = new_index
                    should_play_beep = True
            elif event.name == 'enter':
                return options[selected_index]
            
            if should_play_beep:
                try:
                    winsound.Beep(600, 130)
                except Exception:
                    pass
            
            time.sleep(0.05)

def register_menu():
    while True:
        choice = interactive_menu(
            "REGISTER & START",
            ["START MATCH" ,"SIGN UP", "LOGIN", "BACK TO MAIN MENU"]
        )

        if choice == "SIGN UP":
            signup()
        elif choice == "START MATCH":

            if len(ready_players) == 4:
                start_game_logic()
            else:
                print(f"Cannot start yet! Only {len(ready_players)}/4 players are logged in.")
                print(f"Current list: {ready_players}")
                time.sleep(1) 
                input("Press Enter to continue...")
        elif choice == "LOGIN":
            login()
        elif choice == "BACK TO MAIN MENU":
            return 
    
def loadgame_menu():
    while True:
        choice = interactive_menu(
            "LOAD GAME",
            ["LOGIN","START", "BACK TO MAIN MENU"]
        )

        if choice == "LOGIN":
            login()
        elif choice == "START":
            
            if len(ready_players) == 4:
            
                start_game_logic()
            else:
                print(f"\033[91mCannot start yet! Only {len(ready_players)}/4 players are logged in.\033[0m")
                print(f"Current list: {ready_players}")
                time.sleep(1)

                input("Press Enter to continue...")
        elif choice == "BACK TO MAIN MENU":
            return

def main_menu():
    while True:
        choice = interactive_menu(
            "MAIN MENU",
            ["NEW GAME", "LOAD GAME", "LEADERBOARD", "EXIT"]
        )

        if choice == "NEW GAME":
            register_menu()
        elif choice == "LOAD GAME":
            loadgame_menu()
        elif choice == "LEADERBOARD":
            score_leaderboard()
        elif choice == "EXIT":
            ready_players.clear()
            show_message("GOODBYE", "See you next time!", DARK_BLUE)
            break 
def pause_menu():
    
    while True:
        choice = interactive_menu(
            "PAUSE MENU",
            ["RESUME GAME", "SHOW LEADERBOARD", "SAVE & EXIT"]
        )

        if choice == "RESUME GAME":
            break
        elif choice == "SHOW LEADERBOARD":
            score_leaderboard()
        elif choice == "SAVE & EXIT":
            print("Saving game state...") 
            print("All players logged out.")
            time.sleep(1)
            ready_players.clear()
            break

main_menu()

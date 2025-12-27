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
from rich.console import Console
from rich.panel import Panel
console = Console()



FILE_PATH = "players.json"

ready_players = []

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
    print("\033[1m★ GAME STARTED! ★\033[0m")
    print(f"Players in match: {', '.join(ready_players)}")
    #تابع موقت منطق بازی که بعد از مرج، تابع اصلی جایگزین میشود

def signup():

    

    os.system('cls' if os.name == 'nt' else 'clear')
    print("[magenta]\033[1m༼ つ ◕_◕ ༽つ Sign Up\033[0m[/magenta]")
    
    players = load_players()

    if len(players) >= 4:
        print("[red]Maximum player limit reached (4).[/red]")
        input("Press Enter to continue...")
        return

    username = ""
    while not username:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("[magenta]\033[1m༼ つ ◕_◕ ༽つ Sign Up\033[0m[/magenta]") 
        username = console.input("[bold blue]Enter username: [/bold blue]").strip()

    while True:
             
        email=console.input("[bold blue]Enter email: [/bold blue]").strip()
        valid, msg = check_email_signup(email)
        if valid:
            break
        else:
            print(f"[red]Error: {msg}[/red]")
            print("[yellow]Please try again in 3 seconds...[/yellow]")
            for step in track(range(3)):
                sleep(1)
                step 
            

    while True:
        password=console.input("[bold blue]Enter password: [/bold blue]").strip()
        valid, msg = check_pass(password)
        if valid:
            break
        else:
            print(f"[red]Error: {msg}[/red]")
            print("[yellow]Please try again in 3 seconds...[/yellow]")
            for step in track(range(3)):
                sleep(1)
                step 

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
        "Estate": []
    }

    players.append(new_player)
    save_players(players)

    print(f"[yellow]Player {username} registered successfully![/yellow]")
    console.input("[bold yellow]Press Enter to continue...[/bold yellow]") 

def login():

   

    os.system('cls' if os.name == 'nt' else 'clear')
    print("[blue]\033[1m༼ つ ◕_◕ ༽つ LOGIN\033[0m[/blue]")
    
    players = load_players() 

    username_input = console.input("[bold blue]Enter username: [/bold blue]").strip()
    password_input = console.input("[bold blue]Enter password: [/bold blue]").strip()

    found_user = None
    for player in players:
        if player.get('Username') == username_input:
            found_user = player
            break

    if found_user is None:
        print("[red]User not found![/red]")
        console.input("[bold yellow]Press Enter to continue...[/bold yellow]")
        return None  

    input_bytes = password_input.encode('utf-8')
    stored_hash_bytes = found_user.get('Password', '').encode('utf-8')

    if bcrypt.checkpw(input_bytes, stored_hash_bytes):

        print(f"[cyan]Welcome back, {username_input}![/cyan]")

        if username_input not in ready_players:
            if len(ready_players) < 4:
                ready_players.append(username_input)
                print(f"[cyan]\033[92m[+] {username_input} added to ready list.\033[0m[/cyan]")
                print(f"[cyan]Ready Players ({len(ready_players)}/4): {ready_players}[/cyan]")
            else:
                print("[red]Lobby is full! Cannot add more players.[/red]")
        else:
            print(f"[cyan]User {username_input} is already logged in and ready.[/cyan]")
        time.sleep(0.5)
        console.input("[bold yellow]Press Enter to continue...[/bold yellow]")
        return found_user 
    else:
        print("[red]Incorrect password![/red]")
        console.input("[bold yellow]Press Enter to continue...[/bold yellow]")
        return None

def interactive_menu(title, options):
    
    selected_index = 0
    
    time.sleep(0.2) 

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        console.print(f"[bold cyan]{title}[/bold cyan]")
        print("")
        for i, option in enumerate(options):
            if i == selected_index:
                panel = Panel(option, style="bold cyan", border_style="cyan", padding=(0, 1), expand=False)
                console.print(panel)
            else:
                print(f"    [magenta]{option}[/magenta]")
        
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            
            should_play_beep = False

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
            "\033[1m༼ つ ◕_◕ ༽つ Register & Start\033[0m",
            ["● Start" ,"● Signup", "● Login", "● Back to Main Menu"]
        )

        if choice == "● Signup":
            signup()
        elif choice == "● Start":

            if len(ready_players) == 4:
                start_game_logic()
            else:
                print(f"\033[91mCannot start yet! Only {len(ready_players)}/4 players are logged in.\033[0m")
                print(f"Current list: {ready_players}")
                time.sleep(1) 
                input("Press Enter to continue...")
        elif choice == "● Login":
            login()
        elif choice == "● Back to Main Menu":
            return 
    
def loadgame_menu():
    while True:
        choice = interactive_menu(
            "\033[1m༼ つ ◕_◕ ༽つ Load Game\033[0m",
            ["● Login","● Start", "● Back to Main Menu"]
        )

        if choice == "● Login":
            login()
        elif choice == "● Start":
            
            if len(ready_players) == 4:
            
                start_game_logic()
            else:
                print(f"\033[91mCannot start yet! Only {len(ready_players)}/4 players are logged in.\033[0m")
                print(f"Current list: {ready_players}")
                time.sleep(1)

                input("Press Enter to continue...")
        elif choice == "● Back to Main Menu":
            return

def main_menu():
    while True:
        choice = interactive_menu(
            "\033[1m༼ つ ◕_◕ ༽つ MONOPOLY\033[0m",
            ["● New Game", "● Load Game", "● Leaderboard", "● Exit"]
        )

        if choice == "● New Game":
            register_menu()
        elif choice == "● Load Game":
            loadgame_menu()
        elif choice == "● Leaderboard":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Leaderboard selected (Not implemented yet)")
            input("Press Enter to return...")
        elif choice == "● Exit":
            ready_players.clear()
            print("All players logged out.")
            print("Good Bye!")
            time.sleep(1)
            break 
def pause_menu():
    
    while True:
        choice = interactive_menu(
            f"\033[1m༼ つ ◕_◕ ༽つPause Menu\033[0m",
            ["● Resume Game", "● Show Leaderboard", "● Save & Exit"]
        )

        if choice == "● Resume Game":
            return "resume" 
        elif choice == "● Show Leaderboard":
            print("show_leaderboard")
        elif choice == "● Save & Exit":
            print("Saving game state...") 
            print("All players logged out.")
            time.sleep(1)
            ready_players.clear()
            break

main_menu()
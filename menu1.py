import json
import os
import re
import uuid
import bcrypt
import keyboard  
import time
import winsound     

FILE_PATH = "players.json"

def load_players():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    return []

def save_players(players):
    with open(FILE_PATH, "w") as f:
        json.dump(players, f, indent=4)

def is_valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))
def check_email_signup(email):
    players = load_players()
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not re.match(pattern, email):
        return False, "(；￣Д￣)？Invalid email format."

    if email in [player["email"] for player in players]:
        return False, "This email is already registered"

    return True, "Email accepted."

def check_pass(password):
   if len(password) < 8:
      return False, "┐(ﾟ～ﾟ)┌ Password must be longer than 8 characters"
   if " " in password:
      return False, "┐(-。-;)┌ The password must not contain spaces"
   if not re.search(r"[!@#$%^&*]", password):
      return False, "(@_@;)The password must contain at least one of these characters: ! @ # $ % ^ & *"
   if not re.search(r"\d", password):
      return False, "(?_?)The password must contain at least one number"
   return True, "(^-^; Password accepted"

def signup():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1m༼ つ ◕_◕ ༽つ Sign Up\033[0m")
    
    players = load_players()

    if len(players) >= 4:
        print("Maximum player limit reached (4).")
        input("Press Enter to continue...")
        return

    username = input("Enter username: ").strip()

    while True:      
        email=input("Enter email: ").strip()
        valid, msg = check_email_signup(email)
        if valid:
            break
        else:
            print(f"Error: {msg}")

    while True:
        password=input("Enter password: ").strip()
        valid, msg = check_pass(password)
        if valid:
            break
        else:
            print(f"Error: {msg}")

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

    print(f"Player {username} registered successfully!")
    input("Press Enter to continue...") 

def login():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\033[1m༼ つ ◕_◕ ༽つ LOGIN\033[0m")
    
    players = load_players() 

    username_input = input("Enter username: ").strip()
    password_input = input("Enter password: ").strip()

    found_user = None
    for player in players:
        if player.get('Username') == username_input:
            found_user = player
            break

    if found_user is None:
        print("User not found!")
        input("Press Enter to continue...")
        return None  

    input_bytes = password_input.encode('utf-8')
    stored_hash_bytes = found_user.get('Password', '').encode('utf-8')

    if bcrypt.checkpw(input_bytes, stored_hash_bytes):
        print(f"Welcome back, {username_input}!")
        time.sleep(0.5)
        input("Press Enter to continue...")
        return found_user 
    else:
        print("Incorrect password!")
        input("Press Enter to continue...")
        return None

def interactive_menu(title, options):
    
    selected_index = 0
    
    time.sleep(0.2) 

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(title)
        print("")
        for i, option in enumerate(options):
            if i == selected_index:
                print(f"> {option}") 
            else:
                print(f"   {option}")
        
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
            ["● Signup", "● Start" ,"● Back to Main Menu"]
        )

        if choice == "● Signup":
            signup()
        elif choice == "● Start":
            print("main()")
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
            print("main()")
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
            print("Good Bye!")
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
            time.sleep(1)
            exit()

main_menu()
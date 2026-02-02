#  Monopoly Python (Backend & CLI)

A comprehensive Python implementation of the classic Monopoly game, focused on robust backend logic, data security, and an engaging Command Line Interface (CLI). This project features a modular architecture, secure user management, and dynamic gameplay.

##  Key Features
* **Rich UI:** Utilizes the `Rich` library to render colorful text, organized tables, and a visually appealing terminal experience.
* **User Security:** Implements `bcrypt` for secure password hashing and `uuid` for unique player identification.
* **JSON Data Management:** Persistent storage for game configurations (`CELLS.json`) and player profiles (`PLAYERS.json`).
* **Audio Feedback:** Integration of `winsound` for system-level sound effects during key game events.
* **Advanced Game Logic:** Dedicated modules for banking, dice mechanics, property management, and special tiles like Jail, Chance, and Community Chest.

---

##  Tech Stack
* **Language:** Python
* **Libraries:**
  
    * `Rich`: For CLI styling and formatting.
    * `Bcrypt`: For encryption and security.
    * `Keyboard`: For real-time user input handling.
    * `Winsound`: For Windows-native sound effects.
    * `JSON`, `OS`, `RE`: For data parsing and system operations.

---

##  Project Structure

###  Core Backend & Logic
* `MAIN.py`: The primary entry point for the game engine.
* `BOARD.py`: Manages the board layout and tile logic.
* `PLAYER.py`: Defines player attributes, inventory, and movement.
* `BANK.py`: Handles financial transactions and asset distribution.
* `ESTATE.py`, `RAILROAD.py`, `COMPANY.py`: Specialized logic for different property types.
* `DICE.py`: RNG-based movement system.

###  Menu & Database
* `menu1.py`: The interface for login, registration, and game setup.
* `PLAYERS.json`: Stores encrypted user credentials and statistics.
* `CELLS.json`: Configuration file for board positions and property values.

---

##  Getting Started

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/AliPakani/monopoly-backend.git](https://github.com/AliPakani/monopoly-backend.git)
   cd monopoly-backend
2. **Install dependencies:**
   ```bash
   pip install rich bcrypt keyboard
3. **Run the game:**
   ```bash
   python MENU.py
   
---

##  Contributors

* **Ali Pakani** - Project Lead & Backend Architecture
* **mehrdadab** - Backend Engine & Core Logic
* **lp-parmis** - Menu UI, Game Aesthetics & Color Styling
* **Floraavn** - Error Handling, Debugging & Quality Assurance
* **MehdiShvp** - Menu UI & User Input Validation

---

##  License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

**Copyright (c) 2026:**
* **Ali Pakani**
* **mehrdadab**
* **lp-parmis**
* **Floraavn**
* **MehdiShvp**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files...

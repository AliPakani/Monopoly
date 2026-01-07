from PLAYER import Deposit

def Position(Username) :
    if Username["Position"] > 40 :
        Username["Position"] %= 40
        Deposit(Username, 200)
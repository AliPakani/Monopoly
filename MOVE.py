from PLAYER import Deposit

def Position(Username) :
    try :
        if Username["Position"] > 40 :
            Username["Position"] %= 40
            Deposit(Username, 200)
    except Exception as e :
        print(f"Error : {e}")
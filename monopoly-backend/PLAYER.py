from ESTATE import Find_Price

def Bankrupt(Username) :
    Username["Status"] = "Bankrupt"
    print(f"Hey {Username["Username"]}! You got bankrupt!")

def Dedute(Username, amount) :
    Username["Balance"] -= amount
    print(f"{amount}$ deducted from {Username["Username"]}'s balance!")


def Deposit(Username, Amount) :
    Username["Balance"] += Amount
    print(f"{Amount}$ added to {Username["Username"]}'s balance!")



def Buy(Username, Estate) :
    Username["Estate"].append(Estate)
    Estate["Owner"] = Username["Username"]

def Sell(Username, Estate) :
    I = Username["Estate"].index(Estate)
    Username["Estate"].pop(I)


def Assest(Username) :                                      #جمغ کل دارایی ها
    Sum = 0
    for Estate in Username["Estate"] :
        Sum += Find_Price(Estate)
    return Sum + Username["Balance"]


def Go_To_Jail(Username) :
    Username["Position"] = 11
    Username["Arrested"] = True
    print("You went to jail!")

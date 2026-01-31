import json
from PLAYER import Bankrupt, Dedute, Deposit, Buy, Sell, Assest
from ESTATE import Find_Price, Find_Estate


def Check_Balance(Username, amount) :
    try :
        if Username["Balance"] >= amount :
            return 1
        else :
            return 0
    except Exception as e :
        print(f"Error : {e}")
        return 0

def Check_Assest(Username, AssestList) :                    #جمع قیمت اموال انتخاب شده
    Sum = 0
    try :
        for Estate in AssestList :
            Sum += Find_Price(Estate)
        return Sum
    except Exception as e :
        print(f"Error : {e}")
        return 0


def Check_Rent(Username, Amount):
    if Check_Balance(Username, Amount) == 1 :
        Dedute(Username, Amount)
        Username["Arrested"] = False
        return 1
    else :
        if Assest(Username) // 2 > Amount :                             
            AssestList = []
            Debt = 0
            while Debt < Amount :                                  
                Debt = Check_Assest(Username, AssestList)
                if Debt >= Amount:
                    break
                while True :
                    try :
                        EstateList = []
                        estate = input("Which estate do you want to sell?")
                        if not estate:
                            print("please enter a number")
                            continue
                        EstateList = []
                        for index in estate.split():
                            try:
                                EstateList.append(int(index))
                            except ValueError:
                                print(f"please enter numbers only")
                        if not EstateList:
                            print("No valid numbers entered")
                            continue
                        break
                    except Exception as e:
                        print(f"Error: {e}")
                        continue
                try :
                    AssestList = Find_Estate(EstateList)
                    if not AssestList :
                        print("this is not your property")
                        continue
                except Exception as e :
                    print(f"Error : {e}")

            Deposit(Username, Debt)
            for Estate in AssestList :                              
                Sell(Username, Estate)
                Dedute(Username, Amount)
            Username["Arrested"] = False
            return 1
        else :
            Bankrupt(Username)
            return 0

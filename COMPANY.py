def Company_Buy(Username, Number, Cell) :
    Company = [13, 29]
    if Number in Company :
        Username["Company"].append(Cell)


def Company_Rent(Username, Owner, Number) :
    Company = [13, 29]
    Amount = 0
    try :
        if Number in Company :
            if len(Owner["Company"]) == 1 :
                Amount = sum(Username["Dice"]) * 4
            elif len(Owner["Company"]) == 2 :
                Amount = sum(Username["Dice"]) * 10
            return Amount
        else :
            return Amount
    except Exception as e :
        print(f"Error : {e}")
def Railroad(Username, Number, Cell) :
    Road = [6, 16, 26, 36]
    try :
        if Number in Road :
            Username["Railroad"].append(Cell)
            if len(Username["Railroad"]) > 1 :
                for Railroad in Username["Railroad"] :
                    Railroad["Rent"][0] *= 2
    except Exception as e:
        print(f"Error : {e}")
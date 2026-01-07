def Railroad(Username, Number, Cell) :
    Road = [6, 16, 26, 36]
    if Number in Road :
        Username["Railroad"].append(Cell)
        if len(Username["Railroad"]) > 1 :
            for Railroad in Username["Railroad"] :
                Railroad["Rent"][0] *= 2
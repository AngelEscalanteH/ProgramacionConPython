def get_leter(usedLeters): 
    leter = "1"

    while not leter.isalpha() or len(leter) != 1:
        leter = input("Choose a letter: ").upper()

        if leter in usedLeters:
            print("You have used this leter before")
        elif not leter.isalpha():
            print("Use a leter")
        elif len(leter) != 1:
            print("Use only one leter")

    return leter
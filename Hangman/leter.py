def get_leter(): 
    leter = "1"

    while not leter.isalpha() or len(leter) != 1:
        leter = input("Choose a letter: ").upper()

        if not leter.isalpha():
            print("Use a leter")
        elif len(leter) != 1:
            print("Use only one leter")

    return leter
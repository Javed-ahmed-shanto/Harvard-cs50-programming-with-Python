name = input("What's your name?")

match name:
    case "Harry" | "Hermeone" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
day = input("Enter a day: ").lower()

match day:
    case "Monday":
        print("ugh its monday")
    case "tuesday":
        print ("day of work")
    case "wednesday":
        print ("day of work")
    case "thursday":
        print("day of the work")
    case "friday":
        print("day for musjid")
    case "saturday":
        print("day for sabath")
    case "sunday":
        print("day for catholic")
    case _:
        print ("wrong there no day like this")
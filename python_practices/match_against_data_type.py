value = input("Enter a value (number or string): ")
match value:
    case int():
        print("You entered an integer value:",value)
    case str():
        print("You entered an string value: ",value)
    case _:
        print("Invalid data type entered")
        
while True:
    number = int(raw_input("Enter a number:"))
    check = int(raw_input("Give me another number to divide by:"))

    if number % 2 == 0:
        print ("{0} is an Even Number").format(number)
    elif number % 4 == 0:
        print ("{0} is a multiple of 4").format(number)
    else:
        print("{0} is odd").format(number or number2)
    if number % check == 0:
        print("{0} divides evenly by {1}").format(number, check)
    else:
        print(number, "does not divide evenly by", check)

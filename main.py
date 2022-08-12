# taking inputs from user
def repeat():
    a = int(input("Enter 1st num: "))
    b = input("Enter the operator/sign: ")
    c = int(input("Enter 2nd num: "))
    print("Your equation is        :", a, b, c)
    e = str(input("You want result type    : 'Y' \nYou want to change some\nthings in equation type : 'C' \nor you want to quit     : 'Q'  \n    Enter               : "))

    # putting inputs in math forms and printing result
    if e == "y":
        if b == "+":
            print("Your answer is --> ", a + c)
        elif b == "-":
            print("Your answer is -->", a - c)
        elif b == "/":
            print("Your answer is -->", a / c)
        elif b == "*":
            print("Your answer is -->", a * c)
        elif b == "//":
            print("Your answer is -->", a // c)
        elif b == "%":
            print("Your answer is -->", a % c)
        elif b == "**":
            print("Your answer is -->", a ** c)
        else:
            print("Invalid operator")
    elif e == "c":
        repeat()
    else:
        quit(print("Bye bye..."))
repeat()

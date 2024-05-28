def calculate():
    operation = input('''Operation to be performed
                      + for Addition"
                      - for Subtraction"
                      * for Multiplication
                      / for Division
        ''')

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "+":
        print("{} + {} = {}".format(a,b,a+b))
    elif operation == "-":
        print("{} - {} = {}".format(a,b,a-b))
    elif operation == "*":
        print("{} * {} = {}".format(a,b,a*b))
    elif operation == "/":
        if b != 0:
            print("{} / {} = {}".format(a,b,a/b))
        else:
            print("Cannot be divided by Zero")
    else:
        print("You have entered invalid Operator, please run the program again")

    again = input("Do you want to perform other operation again?(Yes/No): ")
    if again.lower() == "yes":
        calculate()
    else:
        print("Good Bye")

calculate()

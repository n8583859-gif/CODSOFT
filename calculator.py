                                    ###..Simple Calculator..###


#Start calculator interface
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("                  Simple Calculator                       ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")



#Validate proceed or quit choice
while True:
    choice = input("Press `ENTER` to start a calculation\nType 'q' to quit\nYour choice: ").lower()
    if (choice == 'q'):
        print("Thanks for using the calculator. See you next time!")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        proceed = False
        break
    elif (choice == ""):
        proceed = True
        break
    else:
        continue



#Number and operator inputs, Calcuations, Result, Restart
while proceed:

    #Validate first number input from user
    while True:
        try:
            num1 = float(input("Enter the first number: "))
        except ValueError as ve:
            print("⚠️  Please! try again with a valid number.")
            continue
        else:
            break


    #Validate operator input from user
    while True:
        operator = input("Choose an operation (+, -, *, /):").strip()
        if operator not in ('+', '-', '*', '/'):
            print("⚠️  Invalid operation. Please choose from +, -, *, /")
            continue
        else:
            break


    #Validate second number input from user
    while True:
        try:
            num2 = float(input("Enter the second number: "))
        except ValueError as ve:
            print("⚠️  Please! try again with a valid number.")
            continue
        else:
            break
    

    #Addition
    if (operator == '+'):
        result = num1 + num2


    #Diffrence
    if (operator == '-'):
        result = num1 - num2


    #Multiplication
    if (operator == '*'):
        result = num1 * num2


    #Division
    if (operator == '/'):
        #ZeroDivisionError
        if (num2 == 0):
            print("⚠️  Division by zero is not defined.")
            continue
        else:
            result = num1 / num2
    

    #Result printing
    print("--------------------[RESULT]--------------------")
    print(f"|  {num1} {operator} {num2} = {result:.2f}")
    print("------------------------------------------------")


    #Restart calculator
    while True:
        restart = input("Would you like to calculate again? (y/n): ").lower()
        if (restart == 'n'):
            print("Thanks for using the calculator. See you next time!")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            proceed = False
            break
        elif (restart == 'y'):
            proceed = True
            break
        else:
            continue

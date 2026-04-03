                                    ###..Simple Calculator..###


#Start calculator interface
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("                  Simple Calculator                       ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")



#Validate proceed or quit choice
while True:
    choice = input("Press `ENTER` to start a calculation or Type 'q' to quite: ").lower()
    if (choice == 'q'):
        print("\n----------------------------------------------------------")
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
            num1 = float(input("\nEnter the first number: "))
        except ValueError as ve:
            print("⚠️  Please! try again with a valid number.\n")
            continue
        else:
            break


    #Validate operator input from user
    while True:
        operator = input("\nChoose an operation (+, -, *, /):").strip()
        if operator not in ('+', '-', '*', '/'):
            print("⚠️  Invalid operation. Please choose from +, -, *,/ \n")
            continue
        else:
            break


    #Validate second number input from user
    while True:
        try:
            num2 = float(input("\nEnter the second number: "))
            if (num2 == 0):
                raise ZeroDivisionError

        #ValueError handaling
        except ValueError:
            print("⚠️  Please! try again with a valid number.\n")
            continue

        #ZeroDivisionError handaling
        except ZeroDivisionError:
            print("⚠️  Division by zero is not defined.\n")
            continue
        else:
            break


    #(Calculations)
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
        result = num1 / num2



    #Result printing
    print("\n--------------------[RESULT]--------------------")
    print(f"|  {num1} {operator} {num2} = {result:.2f}")
    print("------------------------------------------------\n")


    #Restart calculator
    while True:
        restart = input("Would you like to calculate again? (y/n): ").lower()
        if (restart == 'n'):
            print("------------------------------------------------")
            print("Thanks for using the calculator. See you next time!")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            proceed = False
            break
        elif (restart == 'y'):
            print("\n================================================")
            proceed = True
            break
        else:
            continue

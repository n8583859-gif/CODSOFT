                                    # Calculator with simple functionality


while True:
    #quit or procced options
    print("\n===========================================================")
    process = input("Click `enter` to porceed or `q` to quit: \n").lower()

    #procced or quit
    if (process == "q"):
        print("\nThanks for aproacohng us! \n Have a good day/night...")
        print("___________________________________________________________")
        break

    elif (process == ""):
        #input validation
        try:
            #user input for num1 and operator
            num1 = float(input("Enter first number: "))
            operator = input("Enter an operator (+,-,*,/): ").strip()

            #handle input wrong operator
            if operator not in ("+", "-", "*", "/"):
                print("\n⚠️  Please! Choose operator form (+, -, *, /)\n")
                continue

            #user input for num2
            num2 = float(input("Enter second number: ")) 
            
        #handle error form user
        except ValueError as ve:
            print("\n⚠️  Please! Enter a valid number\n")

        #calculation, result
        else:
            if (operator == "+"):
                    result = num1 + num2
            elif (operator == "-"):
                result = num1 - num2
            elif (operator == "/"):
                #Handling `ZeroDivisionError`
                if (num2 == 0):
                    print("\n⚠️  Division by zero is not defined\n")
                    continue
                else:    
                    result = num1/num2
            else:
                result = num1*num2

            #Print result
            print("\n---------------[RESULT]---------------")
            print(f"{num1} {operator} {num2} = {result}")
            print("--------------------------------------\n")
    
    #revisit `procced or quit options`
    else:
        continue
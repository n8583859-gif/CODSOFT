                                    # Calculator with simple functionality


while True:
    #Quit or procced 
    print("\n===========================================================")
    process = input("Click `enter` to porceed or `q` to quit: \n").lower()
    if (process == "q"):

        print("\nThanks for aproacohng us! \n Have a good day/night...")
        print("___________________________________________________________")
        break
    elif (process == ""):
        pass
    else:
        continue

    #Input validation
    try:
        #User input for num1 and operator
        num1 = float(input("Enter first number: "))
        operator = input("Enter an operator (+,-,*,/): ").strip()

        #Handle input wrong operator
        if operator not in ("+", "-", "*", "/"):
            print("\nPlease! Choose operator form (+, -, *, /)\n")
            continue

        #User input for num2
        num2 = float(input("Enter second number: ")) 
        
    #Handle error form user
    except ValueError as ve:
        print("\nPlease! Enter a valid number\n")

    #Calculation, result
    else:
        if (operator == "+"):
                result = num1 + num2
        elif (operator == "-"):
            result = num1 - num2
        elif (operator == "/"):
            #Handling `ZeroDivisionError`
            if (num2 == 0):
                print("\nDivision by zero is not defined\n")
                continue
            else:    
                result = num1/num2
        else:
            result = num1*num2

        #Print result
        print("\n---------------[RESULT]---------------")
        print(f"{num1} {operator} {num2} = {result}")
        print("--------------------------------------\n")
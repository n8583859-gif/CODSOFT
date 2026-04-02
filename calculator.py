                                    # Calculator with simple functionality


while True:
    #Quit or procced 
    process = input("\nClick `enter` to porceed or `q` to quit: \n").lower()
    if (process == "q"):
        break
    elif (process == ""):
        pass
    else:
        continue

    #Error handle
    try:
        #User input for numbers and operator
        num1 = float(input("Enter first number: "))
        operator = input("Choose an operator (+,-,*,/): ").strip()

        ##Handle wrong operator case
        if operator not in ("+", "-", "*", "/"):
            print("\nPlease! Choose operator form (+, -, *, /)\n")
            continue

        ##User input
        num2 = float(input("Enter second number: ")) 
        
    #Handle error form user
    except ValueError as ve:
        print("\nPlease! Enter a Valid Number\n")

    else:
        #Calculation if no error found
        if (operator == "+"):
                result = num1 + num2
        elif (operator == "-"):
            result = num1 - num2
        elif (operator == "/"):
            #Handling `ZeroDivisionError`
            if (num2 == 0):
                print("\nDivision By Zero Is Not Allowed\n")
                continue
            else:    
                result = num1/num2
        else:
            result = num1*num2

        #Print calculated result
        print(f"{num1} {operator} {num2} = {result}")
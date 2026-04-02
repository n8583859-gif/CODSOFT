                                    # Calculator with simple functionality


while True:
    try:
        #User input
        num1 = float(input("Enter first number: "))
        operator = input("Choose an operator (+,-,*,/): ").strip()

        ##Handle wrong operator case
        if operator not in ("+", "-", "*", "/"):
            print("Please! Choose operator form (+, -, *, /)")
            continue

        ##User input
        num2 = float(input("Enter second number: ")) 
        
    #Handle error form user
    except ValueError as ve:
        print("Please! Enter a Valid Number")

    else:
        #Calculation if no error found
        if (operator == "+"):
                result = num1 + num2
        elif (operator == "-"):
            result = num1 - num2
        elif (operator == "/"):
            #Handling `ZeroDivisionError`
            if (num2 == 0):
                print("Division By Zero Is Not Allowed")
                continue
            else:    
                result = num1/num2
        else:
            result = num1*num2

        #Print calculated result
        print(f"{num1} {operator} {num2} = {result}")
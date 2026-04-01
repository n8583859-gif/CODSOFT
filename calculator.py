                                    # Calculator with simple functionality

#User input
num1 = float(input("Enter first number: "))
operator = input("Choose an operator (+,-,*,/): ").strip()
num2 = float(input("Enter second number: "))

#Calculation
if (operator == "+"):
        result = num1 + num2
elif (operator == "-"):
    result = num1 - num2
elif (operator == "/"):
    #Handling `ZeroDivisionError`
    if (num2 == 0):
         print("Division By Zero Is Not Allowed")
    else:    
        result = num1/num2
else:
    result = num1*num2

#Print calculated result
print(f"{num1} {operator} {num2} = {result}")
